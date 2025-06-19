# Goal of this script is to identify duplicate images in the projects's images directory. This is default path from position of this script: ../../../static/images/*

# find all duplicate images even if they are in subdirectories or filenames doesn't match

# to identify similarity between images use visual transformer, turn image into vector, add them to faiss library, then find duplicates

# print just first 100 duplicates

# Goal of this script is to identify duplicate images in the projects's images directory. This is default path from position of this script: ../../../static/images/*

# find all duplicate images even if they are in subdirectories or filenames doesn't match

# to identify similarity between images use visual transformer, turn image into vector, add them to faiss library, then find duplicates

# print just first 100 duplicates

# Before running, install the required libraries:
# pip install torch transformers Pillow faiss-cpu tqdm

import os
from pathlib import Path
from PIL import Image
import torch
from transformers import ViTFeatureExtractor, ViTModel
import faiss
import numpy as np
from tqdm import tqdm
import datetime

# --- Configuration ---
SCRIPT_DIR = Path(__file__).parent.resolve()
IMAGE_DIR = SCRIPT_DIR / "../../../static/images"
MODEL_NAME = 'google/vit-base-patch16-224-in21k'
DUPLICATE_LIMIT = 1000
# Threshold for considering images as duplicates. Lower is stricter.
# For perfect duplicates, the L2 distance will be 0 after normalization.
SIMILARITY_THRESHOLD = 1e-5

def find_image_files(directory):
    """Recursively finds all image files in a directory."""
    supported_extensions = ("*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.webp")
    image_paths = []
    for ext in supported_extensions:
        all_files = list(Path(directory).rglob(ext))
        # Filter out images in /processed/ folders
        filtered_files = [p for p in all_files if "/processed/" not in str(p) and "\\processed\\" not in str(p)]
        image_paths.extend(filtered_files)
    print(f"Found {len(image_paths)} images in '{directory}' (excluding /processed/ folder).")
    return image_paths

def load_model():
    """Loads the Vision Transformer model and feature extractor."""
    print(f"Loading model '{MODEL_NAME}'...")
    # Prefer GPU if available, with support for Apple Silicon (MPS)
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    print(f"Using device: {device}")

    feature_extractor = ViTFeatureExtractor.from_pretrained(MODEL_NAME)
    model = ViTModel.from_pretrained(MODEL_NAME).to(device)
    model.eval()
    return feature_extractor, model, device

def extract_features(image_path, feature_extractor, model, device):
    """Extracts a feature vector from a single image."""
    try:
        img = Image.open(image_path).convert("RGB")
        inputs = feature_extractor(images=img, return_tensors="pt").to(device)
        with torch.no_grad():
            outputs = model(**inputs)
            # Use the mean of the last hidden state as the feature vector
            features = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
        return features
    except Exception as e:
        print(f"Warning: Could not process image {image_path}. Error: {e}")
        return None

def get_all_embeddings(image_paths, feature_extractor, model, device):
    """Extracts embeddings for a list of image paths."""
    embeddings = []
    valid_paths = []
    print("Extracting features from images...")
    for path in tqdm(image_paths, desc="Processing images"):
        feature_vector = extract_features(path, feature_extractor, model, device)
        if feature_vector is not None:
            embeddings.append(feature_vector)
            valid_paths.append(path)
    return np.array(embeddings).astype('float32'), valid_paths

def find_duplicate_groups(embeddings, image_paths):
    """Uses FAISS to find and group duplicate images."""
    if not embeddings.any():
        print("No embeddings were generated. Exiting.")
        return []

    dimension = embeddings.shape[1]
    print(f"\nBuilding FAISS index with dimension {dimension}...")
    index = faiss.IndexFlatL2(dimension)

    # Normalize embeddings for stable L2 distance comparison
    faiss.normalize_L2(embeddings)
    index.add(embeddings)

    print(f"Searching for duplicates in {index.ntotal} vectors...")
    duplicate_groups = []
    processed_indices = set()

    for i in range(index.ntotal):
        if i in processed_indices:
            continue

        # Find all vectors within the similarity threshold of the current vector
        lims, _, I_single = index.range_search(embeddings[i:i+1], SIMILARITY_THRESHOLD)

        # Group contains more than the item itself
        if lims[1] > 1:
            group_indices = set(I_single)
            # Ensure we haven't processed any member of this group before
            if not processed_indices.intersection(group_indices):
                group_paths = {str(image_paths[idx]) for idx in group_indices}
                duplicate_groups.append(list(group_paths))
                processed_indices.update(group_indices)

        if len(duplicate_groups) >= DUPLICATE_LIMIT:
            break

    return duplicate_groups

def find_unused_images(all_image_paths, project_root):
    """Find images that are not referenced in any markdown files."""
    print("Searching for unused images...")
    content_dir = project_root / 'content'
    unused_images = []
    all_md_content = ""

    # First read all markdown files into a single string for efficient searching
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        all_md_content += f.read()
                except Exception:
                    pass

    # Check each image to see if its filename is referenced anywhere
    for img_path in tqdm(all_image_paths, desc="Checking image usage"):
        image_filename = os.path.basename(img_path)
        if image_filename not in all_md_content:
            unused_images.append(img_path)

    return unused_images

if __name__ == "__main__":
    if not IMAGE_DIR.exists() or not IMAGE_DIR.is_dir():
        print(f"Error: Image directory not found at '{IMAGE_DIR}'")
    else:
        # Get project root for relative paths
        project_root = SCRIPT_DIR.parent.parent.parent.resolve()

        all_image_paths = find_image_files(IMAGE_DIR)

        if not all_image_paths:
            print("No images found to process.")
        else:
            extractor, vit_model, dev = load_model()
            image_embeddings, valid_image_paths = get_all_embeddings(all_image_paths, extractor, vit_model, dev)
            duplicates = find_duplicate_groups(image_embeddings, valid_image_paths)

            # Find unused images
            unused_images = find_unused_images(all_image_paths, project_root)

            if not duplicates:
                print("\nNo duplicates found.")
            else:
                print(f"\n--- Found {len(duplicates)} Duplicate Groups (showing up to {DUPLICATE_LIMIT}) ---")
                for i, group in enumerate(duplicates):
                    print(f"\nGroup {i + 1}:")
                    for path in sorted(group):
                        print(f"  - {path}")
                print("\n--- End of Report ---")

                # Generate HTML report
                report_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                html_path = SCRIPT_DIR / '../../../data/duplicate_images_report.html'
                html_content = [
                    "<html>",
                    "<head><title>Duplicate Images Report</title>",
                    "<style>",
                    "table { border-collapse: collapse; width: 100%; }",
                    "th, td { border: 1px solid #ddd; padding: 8px; text-align: left; vertical-align: top; }",
                    "th { background-color: #f2f2f2; }",
                    "img { max-width: 200px; max-height: 200px; }",
                    "</style>",
                    "</head>",
                    "<body>",
                    f"<h1>Found {len(duplicates)} Duplicate Groups</h1>",
                    f"<p><b>Report generated:</b> {report_time}</p>"
                ]
                for i, group in enumerate(duplicates):
                    html_content.append(f"<h2>Group {i + 1}</h2>")
                    html_content.append("<table>")
                    html_content.append("<tr><th>Image</th><th>Path</th><th>Dimensions</th><th>Used in</th></tr>")
                    for path in sorted(group):
                        # Show path relative to main project folder (workspace root)
                        rel_path_project = os.path.relpath(path, start=project_root)
                        # For <img src>, use path relative to the HTML report location (data/)
                        html_img_path = os.path.relpath(path, start=(project_root / 'data'))
                        try:
                            img = Image.open(path)
                            width, height = img.size
                            size_str = f"{width}x{height}px"
                        except Exception:
                            size_str = "Unknown size"
                        # Find usages in content/*.md files by filename
                        usages = []
                        image_filename = os.path.basename(path)
                        content_dir = project_root / 'content'
                        for root, dirs, files in os.walk(content_dir):
                            for file in files:
                                if file.endswith('.md'):
                                    file_path = os.path.join(root, file)
                                    try:
                                        with open(file_path, 'r', encoding='utf-8') as f:
                                            if image_filename in f.read():
                                                usages.append(os.path.relpath(file_path, start=project_root))
                                    except Exception:
                                        pass
                        usages_html = "<br>".join(usages) if usages else "<i>Not used in content</i>"
                        html_content.append(f"<tr><td><img src='{html_img_path}'></td><td>{rel_path_project}</td><td>{size_str}</td><td>{usages_html}</td></tr>")
                    html_content.append("</table>")

                # Add section for unused images
                html_content.append(f"<h1>Unused Images ({len(unused_images)})</h1>")
                html_content.append("<p>The following images are not referenced in any markdown files in the content directory:</p>")
                html_content.append("<table>")
                html_content.append("<tr><th>Image</th><th>Path</th><th>Dimensions</th></tr>")

                for path in sorted(unused_images):
                    # Show path relative to main project folder (workspace root)
                    rel_path_project = os.path.relpath(path, start=project_root)
                    # For <img src>, use path relative to the HTML report location (data/)
                    html_img_path = os.path.relpath(path, start=(project_root / 'data'))
                    try:
                        img = Image.open(path)
                        width, height = img.size
                        size_str = f"{width}x{height}px"
                    except Exception:
                        size_str = "Unknown size"

                    html_content.append(f"<tr><td><img src='{html_img_path}'></td><td>{rel_path_project}</td><td>{size_str}</td></tr>")

                html_content.append("</table>")

                # Add section with rm commands for unused images
                html_content.append("<h2>Shell Commands to Remove Unused Images</h2>")
                html_content.append("<p>Copy and paste these commands to remove unused images one by one:</p>")
                html_content.append("<pre style='background-color: #f5f5f5; padding: 10px; border-radius: 5px; overflow: auto;'>")

                for path in sorted(unused_images):
                    # Use absolute paths for the rm commands for safety
                    abs_path = str(path).replace("'", "\\'")  # Escape single quotes for shell safety
                    html_content.append(f"rm '{abs_path}'")

                html_content.append("</pre>")

                html_content.append("</body></html>")
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(html_content))
                print(f"\nHTML report generated: {html_path}")

                # Print summary of unused images
                print(f"\n--- Found {len(unused_images)} Unused Images ---")
                print("Check the HTML report for details.")
