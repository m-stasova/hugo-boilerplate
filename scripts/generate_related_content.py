#!/usr/bin/env python3
"""
Generate Related Content YAML

This script indexes content files in a specific language folder as vectors using FAISS
and a sentence transformer model from Hugging Face. For each file, it finds
the 3 most similar files and generates a YAML file with the related content structure.

Usage:
    python generate_related_content.py --lang en

Requirements:
    pip install sentence-transformers faiss-cpu torch pyyaml frontmatter markdown bs4 tqdm
"""

import os
import re
import argparse
import yaml
import gc
import frontmatter
import markdown
from bs4 import BeautifulSoup
from tqdm import tqdm
from collections import defaultdict

# Constants
MODEL_NAME = "all-MiniLM-L6-v2"  # Extremely small model for minimal memory usage
MAX_TEXT_LENGTH = 2000  # Limit text length to avoid memory issues
TOP_K = 3  # Number of related content items to find

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate related content YAML")
    parser.add_argument("--lang", type=str, default="en", help="Language code (e.g., 'en', 'de')")
    parser.add_argument("--content_dir", type=str, default="content", 
                        help="Content directory relative to Hugo root")
    parser.add_argument("--output_dir", type=str, default="data/related_content",
                        help="Output directory for YAML files relative to Hugo root")
    parser.add_argument("--exclude_sections", type=str, nargs="+", default=["_index.md"],
                        help="Sections or files to exclude")
    parser.add_argument("--model", type=str, default=MODEL_NAME,
                        help=f"Model name to use (default: {MODEL_NAME})")
    return parser.parse_args()

def extract_text_from_markdown(content):
    """Extract text content from markdown, removing HTML tags."""
    try:
        # Convert markdown to HTML
        html = markdown.markdown(content)
        # Parse HTML and extract text
        soup = BeautifulSoup(html, 'html.parser')
        # Get text and normalize whitespace
        text = soup.get_text(separator=' ', strip=True)
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    except Exception as e:
        print(f"Error extracting text from markdown: {e}")
        return ""

def process_content_files(hugo_root, lang, content_dir, exclude_sections):
    """Process content files and extract their text content."""
    content_path = os.path.join(hugo_root, content_dir, lang)
    
    if not os.path.exists(content_path):
        print(f"Content path does not exist: {content_path}")
        return []
    
    print(f"Processing content files in: {content_path}")
    
    file_data = []
    
    # Walk through the content directory
    for root, _, files in os.walk(content_path):
        for file in files:
            if file.endswith('.md') and file not in exclude_sections:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, os.path.join(hugo_root, content_dir, lang))
                
                # Read the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        # Parse frontmatter and content
                        post = frontmatter.load(f)
                        
                        # Get the section and slug
                        section_parts = os.path.dirname(rel_path).split(os.sep)
                        section = section_parts[0] if section_parts and section_parts[0] != '.' else ''
                        
                        # Get the slug (filename without extension)
                        slug = os.path.splitext(os.path.basename(rel_path))[0]
                        
                        # Combine title, description, and content for embedding
                        title = post.get('title', '')
                        description = post.get('description', '')
                        term = post.get('term', '')
                        short_description = post.get('shortDescription', '')
                        
                        # Extract text from markdown content - limit to first 1000 chars to save memory
                        content_text = extract_text_from_markdown(post.content[:1000])
                        
                        # Combine all text for embedding
                        combined_text = f"{title} {term} {description} {short_description} {content_text}"
                        
                        # Limit text length to avoid memory issues
                        if len(combined_text) > MAX_TEXT_LENGTH:
                            combined_text = combined_text[:MAX_TEXT_LENGTH]
                        
                        # Store file info
                        file_info = {
                            'path': rel_path,
                            'section': section,
                            'slug': slug,
                            'text': combined_text
                        }
                        
                        file_data.append(file_info)
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")
    
    print(f"Found {len(file_data)} content files")
    return file_data

def generate_embeddings(file_data, model_name):
    """Generate embeddings for the file data using the specified model."""
    print(f"Loading model: {model_name}")
    
    # Import here to delay loading these heavy libraries until needed
    import torch
    import faiss
    from sentence_transformers import SentenceTransformer
    
    # Use CPU explicitly to avoid CUDA memory issues
    model = SentenceTransformer(model_name, device="cpu")
    
    # Process files in very small batches to manage memory
    embeddings = []
    batch_size = 1  # Process one file at a time
    
    for i in range(0, len(file_data), batch_size):
        batch = file_data[i:i+batch_size]
        texts = [info['text'] for info in batch]
        
        print(f"Processing file {i+1}/{len(file_data)}")
        
        # Get embeddings for this batch
        with torch.no_grad():  # Disable gradient calculation to save memory
            batch_embeddings = model.encode(texts, show_progress_bar=False)
        
        embeddings.extend(batch_embeddings)
        
        # Clear batch data to free memory
        texts = None
        batch = None
        
        # Force garbage collection to free memory
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    
    # Free model memory
    del model
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    
    return embeddings

def find_related_content(file_data, embeddings, top_k=TOP_K):
    """Find related content for each file using FAISS."""
    print("Building FAISS index...")
    
    # Import here to delay loading until needed
    import numpy as np
    import faiss
    
    # Convert embeddings to numpy array
    embeddings_array = np.array(embeddings).astype('float32')
    
    # Create and train the index
    dimension = embeddings_array.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_array)
    
    # Find related content for each file
    related_content = defaultdict(lambda: defaultdict(list))
    
    print("Finding related content...")
    for i, file_info in enumerate(tqdm(file_data)):
        section = file_info['section']
        slug = file_info['slug']
        current_path = file_info['path']
        
        # Normalize current path for comparison
        current_normalized_path = current_path
        if current_normalized_path.endswith('.md'):
            current_normalized_path = current_normalized_path[:-3]
        
        # Skip if no section (like root _index.md)
        if not section:
            continue
        
        # Search for similar files
        query_vector = embeddings_array[i].reshape(1, -1)
        # Request more results than we need since we'll filter some out
        search_k = top_k + 5  
        distances, indices = index.search(query_vector, min(search_k, len(file_data)))
        
        # Add related content (excluding the file itself)
        added_count = 0
        for j in indices[0]:
            if added_count >= top_k:
                break
                
            if j < len(file_data):  # Check bounds
                related_file = file_data[j]
                related_path = related_file['path']
                
                # Convert path format: section/file.md -> section/file
                if related_path.endswith('.md'):
                    related_path = related_path[:-3]
                
                # Skip if this is the same file or if the path matches
                if j == i or related_path == current_normalized_path:
                    continue
                
                # Add to related content
                related_content[section][slug].append({
                    'file': related_path
                })
                added_count += 1
    
    # Free memory
    embeddings_array = None
    index = None
    gc.collect()
    
    return related_content

def generate_yaml(related_content, hugo_root, output_dir, lang):
    """Generate YAML file with related content structure."""
    print(f"Generating YAML file for language: {lang}")
    
    # Create output directory if it doesn't exist
    output_path = os.path.join(hugo_root, output_dir)
    os.makedirs(output_path, exist_ok=True)
    
    # Convert defaultdict to regular dict for YAML serialization
    yaml_data = {}
    for section, slugs in related_content.items():
        yaml_data[section] = {}
        for slug, related_files in slugs.items():
            yaml_data[section][slug] = related_files
    
    # Write YAML file
    output_file = os.path.join(output_path, f"{lang}.yaml")
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)
    
    print(f"YAML file generated: {output_file}")

def main():
    """Main function."""
    args = parse_args()
    
    # Get Hugo root directory (parent of script directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    hugo_root = os.path.dirname(script_dir)
    
    print(f"Hugo root: {hugo_root}")
    
    # Process content files
    file_data = process_content_files(
        hugo_root, args.lang, args.content_dir, args.exclude_sections
    )
    
    if not file_data:
        print("No content files found or processed.")
        return
    
    # Generate embeddings
    embeddings = generate_embeddings(file_data, args.model)
    
    # Find related content
    related_content = find_related_content(file_data, embeddings, top_k=TOP_K)
    
    # Free memory
    file_data = None
    embeddings = None
    gc.collect()
    
    # Generate YAML file
    generate_yaml(related_content, hugo_root, args.output_dir, args.lang)

if __name__ == "__main__":
    main()
