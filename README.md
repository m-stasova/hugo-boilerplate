# Hugo Boilerplate

A clean and minimal Hugo boilerplate project that can be used as a starting point for other Hugo projects.

## Prerequisites

- Hugo Extended (v0.145.0 or later)
- Go (for Hugo modules if used)

## Getting Started

1. Clone this repository:
   ```bash
   git clone [repository-url]
   ```

2. Navigate to the project directory:
   ```bash
   cd hugo-boilerplate
   ```

3. Start the Hugo development server:
   ```bash
   hugo server -D
   ```

The site will be available at http://localhost:1313/

## Project Structure

```
.
├── archetypes/        # Content templates
├── assets/            # Files that need processing (SCSS, JS)
├── content/           # Your content files
├── data/             # Configuration files
├── layouts/          # Templates
├── scripts/          # Build and utility scripts
├── static/           # Static files
├── themes/           # Theme files
├── hugo.toml         # Hugo configuration
└── README.md         # This file
```

## Creating Content

To create a new post:
```bash
hugo new content/posts/my-post.md
```

## Customization

1. Modify `hugo.toml` for site configuration
2. Edit templates in `themes/boilerplate/layouts/`
3. Add styles in `themes/boilerplate/assets/`
4. Place static files in `static/`

## Multilingual Support

This boilerplate supports multiple languages with separate domains:

1. Content Structure:
   ```
   content/
   ├── en/          # English content
   │   ├── posts/
   │   └── pages/
   ├── de/          # German content
   │   ├── posts/
   │   └── pages/
   └── _index.md    # Homepage in default language
   ```

2. Language Configuration:
   - Each language has its own domain (e.g., example.com for English, example.de for German)
   - Language-specific settings are in `hugo.toml`
   - Translations are managed in `i18n/*.yaml` files

3. Creating Content:
   ```bash
   # Create content in English
   hugo new content/en/posts/my-post.md
   
   # Create content in German
   hugo new content/de/posts/my-post.md
   ```

## Environment Setup

1. Copy the environment template:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your configuration values. This file is ignored by git for security.

## Building the Project

To build the project for production:
```bash
./scripts/build.sh
```

This script will:
1. Clean the existing build
2. Generate minified production files
3. Perform post-build checks
4. Show build statistics

The built files will be available in the `public/` directory.

## License

MIT License
