import os
import re
import requests
import toml
from pathlib import Path
from urllib.parse import urlparse
import random

CONTENT_DIR = Path(__file__).parents[3] / 'content'
STATIC_IMAGES_DIR = Path(__file__).parents[3] / 'static' / 'images'

IMG_URL_PREFIXES = [
    'http://',
    'https://',
]
IMG_PATTERN = re.compile(
    r'!\[([^\]]*)\]\(((?:' + '|'.join(re.escape(p) for p in IMG_URL_PREFIXES) + r')[^\s)]+)(?:\s+"([^"]+)")?\)'
)
TITLE_PATTERN = re.compile(r'title:\s*"([^"]+)"', re.IGNORECASE)

def url_matches_prefix(url):
    return any(url.startswith(prefix) for prefix in IMG_URL_PREFIXES)

def get_effective_rel_folder(md_path):
    rel_folder = md_path.parent.relative_to(CONTENT_DIR)
    parts = list(rel_folder.parts)
    # Remove language directory if present (e.g., 'en')
    if parts and len(parts[0]) == 2:  # crude check for language code
        parts = parts[1:]
    return Path(*parts)

def find_title_near_line(lines, idx):
    # Search upwards for a title attribute
    for i in range(idx, -1, -1):
        match = TITLE_PATTERN.search(lines[i])
        if match:
            return match.group(1)
    return 'untitled'

def process_md_file(md_path):
    rel_folder = get_effective_rel_folder(md_path)
    md_stem = md_path.stem  # Get the name of the md file without extension
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Split TOML frontmatter and body
    if content.startswith('+++'):
        end_idx = content.find('+++', 3)
        if end_idx != -1:
            toml_section = content[3:end_idx].strip()
            body = content[end_idx+3:]
        else:
            toml_section = ''
            body = content
    else:
        toml_section = ''
        body = content
    changed = False
    toml_changed = False
    body_changed = False
    # Parse TOML frontmatter
    if toml_section:
        try:
            data = toml.loads(toml_section)
        except toml.TomlDecodeError as e:
            print(f"!!! ERROR decoding TOML in {md_path}: {e}")
            return
        # Main image
        if 'image' in data and isinstance(data['image'], str) and url_matches_prefix(data['image']):
            url = data['image']
            ext = os.path.splitext(urlparse(url).path)[1]
            if not ext:
                # Try to get extension from Content-Type header
                resp = requests.head(url, allow_redirects=True)
                content_type = resp.headers.get('Content-Type', '')
                if 'image/' in content_type:
                    ext = '.' + content_type.split('image/')[1].split(';')[0].strip().split('+')[0]
                else:
                    ext = '.jpg'  # fallback
            out_dir = STATIC_IMAGES_DIR / rel_folder
            out_dir.mkdir(parents=True, exist_ok=True)
            # Try to generate a safe title: 1. from TOML 'title', 2. from URL filename, 3. 'untitled'
            orig_title = data.get('title')
            if orig_title and orig_title.strip():
                base_title = orig_title
            else:
                url_path = urlparse(url).path
                url_filename = os.path.splitext(os.path.basename(url_path))[0]
                if url_filename:
                    base_title = url_filename
                else:
                    # Add random number to 'untitled' to make it unique
                    base_title = f"untitled_{random.randint(1000, 9999)}"
            safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', base_title)
            out_filename = f"{md_stem}_{safe_title}{ext}"
            out_path = out_dir / out_filename
            if not out_path.exists():
                resp = requests.get(url)
                resp.raise_for_status()
                with open(out_path, 'wb') as imgf:
                    imgf.write(resp.content)
            local_url = f"/images/{rel_folder}/{out_filename}".replace('\\', '/')
            data['image'] = local_url
            toml_changed = True
            changed = True
        # Cards images
        if 'cards' in data and isinstance(data['cards'], list):
            for card in data['cards']:
                if 'image' in card and isinstance(card['image'], str) and url_matches_prefix(card['image']):
                    url = card['image']
                    ext = os.path.splitext(urlparse(url).path)[1]
                    card_title = card.get('title', 'untitled')
                    safe_card_title = re.sub(r'[^a-zA-Z0-9_-]', '_', card_title)
                    out_filename = f"{md_stem}_{safe_card_title}{ext}"
                    out_dir = STATIC_IMAGES_DIR / rel_folder
                    out_dir.mkdir(parents=True, exist_ok=True)
                    out_path = out_dir / out_filename
                    if not out_path.exists():
                        resp = requests.get(url)
                        resp.raise_for_status()
                        with open(out_path, 'wb') as imgf:
                            imgf.write(resp.content)
                    local_url = f"/images/{rel_folder}/{out_filename}".replace('\\', '/')
                    card['image'] = local_url
                    toml_changed = True
                    changed = True
        if toml_changed:
            new_toml = toml.dumps(data)
        else:
            new_toml = toml_section
    else:
        new_toml = toml_section
    # Process body images
    lines = body.splitlines()
    for idx, line in enumerate(lines):
        # Markdown image syntax
        for match in IMG_PATTERN.finditer(line):
            alt_text = match.group(1)  # Get alt text inside []
            url = match.group(2)
            explicit_title = match.group(3)  # Title after URL in quotes
            
            if not url_matches_prefix(url):
                continue
                
            # Priority: 1. Explicit title in quotes, 2. Alt text, 3. Title from nearby TOML
            title = explicit_title or alt_text or find_title_near_line(lines, idx)
            if not title or title.strip() == '':
                title = 'untitled'
                
            ext = os.path.splitext(urlparse(url).path)[1]
            out_dir = STATIC_IMAGES_DIR / rel_folder
            out_dir.mkdir(parents=True, exist_ok=True)
            safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', title)
            out_filename = f"{md_stem}_{safe_title}{ext}"
            out_path = out_dir / out_filename
            if not out_path.exists():
                resp = requests.get(url)
                resp.raise_for_status()
                with open(out_path, 'wb') as imgf:
                    imgf.write(resp.content)
            local_url = f"/images/{rel_folder}/{out_filename}".replace('\\', '/')
            new_img_md = f'![{alt_text}]({local_url} "{title}")'
            line = line.replace(match.group(0), new_img_md)
            body_changed = True
            changed = True
            
        # Shortcode lazyimg src attribute (single line)
        lazyimg_match = re.search(r'\{\{<\s*lazyimg[^\n]*src="([^"]+)"', line)
        if lazyimg_match:
            url = lazyimg_match.group(1)
            if url_matches_prefix(url):
                # Extract alt attribute if it exists in the shortcode
                alt_match = re.search(r'alt="([^"]+)"', line)
                alt_text = alt_match.group(1) if alt_match else f"lazyimg_{idx}"
                
                ext = os.path.splitext(urlparse(url).path)[1]
                if not ext:
                    # Try to get extension from Content-Type header
                    resp = requests.head(url, allow_redirects=True)
                    content_type = resp.headers.get('Content-Type', '')
                    if 'image/' in content_type:
                        ext = '.' + content_type.split('image/')[1].split(';')[0].strip().split('+')[0]
                    else:
                        ext = '.jpg'  # fallback
                out_dir = STATIC_IMAGES_DIR / rel_folder
                out_dir.mkdir(parents=True, exist_ok=True)
                safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', alt_text)
                out_filename = f"{md_stem}_{safe_title}{ext}"
                out_path = out_dir / out_filename
                if not out_path.exists():
                    resp = requests.get(url)
                    resp.raise_for_status()
                    with open(out_path, 'wb') as imgf:
                        imgf.write(resp.content)
                local_url = f"/images/{rel_folder}/{out_filename}".replace('\\', '/')
                line = re.sub(r'(src=")([^"]+)(")', f'\\1{local_url}\\3', line)
                body_changed = True
                changed = True
        lines[idx] = line
        
    # Handle multi-line lazyimg shortcodes
    full_content = '\n'.join(lines)
    multi_lazyimg_pattern = re.compile(r'\{\{<\s*lazyimg\s+[^>]*?src="([^"]+)"[^>]*?>}}', re.DOTALL)
    for match in multi_lazyimg_pattern.finditer(full_content):
        url = match.group(1)
        if url_matches_prefix(url):
            try:
                # Extract alt attribute if it exists in the shortcode
                shortcode = match.group(0)
                alt_match = re.search(r'alt="([^"]+)"', shortcode)
                alt_text = alt_match.group(1) if alt_match else "lazyimg_multi"
                
                ext = os.path.splitext(urlparse(url).path)[1]
                out_dir = STATIC_IMAGES_DIR / rel_folder
                out_dir.mkdir(parents=True, exist_ok=True)
                safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', alt_text)
                out_filename = f"{md_stem}_{safe_title}{ext}"
                out_path = out_dir / out_filename
                if not out_path.exists():
                    resp = requests.get(url)
                    resp.raise_for_status()
                    with open(out_path, 'wb') as imgf:
                        imgf.write(resp.content)
                local_url = f"/images/{rel_folder}/{out_filename}".replace('\\', '/')
                # Replace just the src attribute value
                new_shortcode = re.sub(r'(src=")([^"]+)(")', f'\\1{local_url}\\3', shortcode)
                full_content = full_content.replace(shortcode, new_shortcode)
                body_changed = True
                changed = True
            except requests.RequestException as e:
                print(f"!!! ERROR downloading image from {url}: {e}")
                return
            
    if body_changed:
        body = full_content
        
    if changed:
        # Write both TOML and body together, always
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"+++\n{new_toml}\n+++\n{body}")

def main():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                process_md_file(Path(root) / file)

if __name__ == '__main__':
    main()
