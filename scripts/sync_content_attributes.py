attributes_to_sync = [
    'image',
    'youtubeVideoID',
    'date',
]

import os
import re
import toml
from pathlib import Path

# Base content directory
content_dir = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../content')))
en_content_dir = content_dir / 'en'

def extract_front_matter(file_path):
    """Extract TOML front matter from markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for front matter between +++ delimiters
    match = re.match(r'^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n', content, re.DOTALL)
    if match:
        front_matter_text = match.group(1)
        try:
            front_matter = toml.loads(front_matter_text)
            remaining_content = content[match.end():]
            return front_matter, remaining_content
        except toml.TomlDecodeError as e:
            print(f"Error parsing front matter in {file_path}: {e}")
            return {}, content
    return {}, content

def update_front_matter(file_path, updated_front_matter, remaining_content):
    """Update TOML front matter in markdown file"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('+++\n')
        f.write(toml.dumps(updated_front_matter))
        f.write('+++\n')
        f.write(remaining_content)
    
def process_file(en_file_path):
    """Process a single English file and update corresponding translations"""
    # Get relative path from content/en
    rel_path = en_file_path.relative_to(en_content_dir)
    
    # Extract front matter from English file
    en_front_matter, _ = extract_front_matter(en_file_path)
    
    # Create a dictionary with only the attributes we want to sync
    sync_attributes = {}
    for attr in attributes_to_sync:
        if attr in en_front_matter:
            sync_attributes[attr] = en_front_matter[attr]
    
    if not sync_attributes:
        return  # Nothing to sync
    
    # Find corresponding files in other language directories
    for lang_dir in content_dir.iterdir():
        if lang_dir.is_dir() and lang_dir.name != 'en':
            translated_file = lang_dir / rel_path
            
            if translated_file.exists():
                # Extract front matter from translated file
                translated_front_matter, remaining_content = extract_front_matter(translated_file)
                
                # Update front matter with synced attributes
                updated = False
                for attr in attributes_to_sync:
                    # Always sync 'date' (add if missing)
                    if attr == 'date':
                        if attr not in translated_front_matter:
                            import datetime
                            translated_front_matter[attr] = en_front_matter.get(attr, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                            updated = True
                        elif attr in en_front_matter and translated_front_matter.get(attr) != en_front_matter[attr]:
                            translated_front_matter[attr] = en_front_matter[attr]
                            updated = True
                    else:
                        # Only sync if present in English version
                        if attr in en_front_matter:
                            if translated_front_matter.get(attr) != en_front_matter[attr]:
                                translated_front_matter[attr] = en_front_matter[attr]
                                updated = True
                
                if updated:
                    print(f"Updating {translated_file}")
                    update_front_matter(translated_file, translated_front_matter, remaining_content)

def main():
    """Main function to sync content attributes"""
    print(f"Syncing content attributes: {', '.join(attributes_to_sync)}")
    
    # Find all markdown files in the English content directory
    for file_path in en_content_dir.glob('**/*.md'):
        if file_path.is_file():
            print(f"Processing {file_path.relative_to(content_dir)}")
            process_file(file_path)
    
    print("Content attributes sync complete.")

if __name__ == "__main__":
    main()
