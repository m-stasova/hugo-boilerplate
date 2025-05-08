import os
import re
import requests
import toml
from pathlib import Path
from urllib.parse import urlparse

CONTENT_DIR = Path(__file__).parents[3] / 'content'
STATIC_IMAGES_DIR = Path(__file__).parents[3] / 'static' / 'images'

IMG_URL_PREFIXES = [
    'https://replicate.delivery/',
    'https://www.wachman.eu/',
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
            out_dir = STATIC_IMAGES_DIR / rel_folder
            out_dir.mkdir(parents=True, exist_ok=True)
            safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', data.get('title', 'untitled'))
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
            
        # Shortcode lazyimg src attribute
        lazyimg_match = re.search(r'\{\{<\s*lazyimg[^\n]*src="([^"]+)"', line)
        if lazyimg_match:
            url = lazyimg_match.group(1)
            if url_matches_prefix(url):
                ext = os.path.splitext(urlparse(url).path)[1]
                out_dir = STATIC_IMAGES_DIR / rel_folder
                out_dir.mkdir(parents=True, exist_ok=True)
                safe_title = f"lazyimg_{idx}"
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
    if changed:
        body = '\n'.join(lines)
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
