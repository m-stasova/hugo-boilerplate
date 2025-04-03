# Hugo Boilerplate Theme

A clean and minimal Hugo theme designed for modern websites with a focus on performance, SEO, and responsive design. This theme includes Tailwind CSS integration, comprehensive SEO features, responsive image processing, and multilingual support out of the box.

## Features

- **Tailwind CSS Integration** - Modern utility-first CSS framework
- **Responsive Design** - Optimized for all device sizes
- **Multilingual Support** - Built-in support for multiple languages
- **SEO Optimized** - Comprehensive metadata and structured data
- **Responsive Images** - Automatic image processing with WebP conversion
- **Lazy Loading** - Performance-optimized image and video loading
- **Glossary System** - Built-in glossary with alphabetical navigation
- **Tag & Category System** - Comprehensive taxonomy management
- **Component Library** - Extensive collection of pre-built components:
  - Headers and navigation menus
  - Product showcases and listings
  - Feature sections
  - Review components
  - Banners and CTAs

## Installation

### Option 1: As a Git Submodule (Recommended)

This method allows you to easily update the theme when new versions are released:

```bash
# Navigate to your Hugo site's root directory
cd your-hugo-site

# Add the theme as a submodule
git submodule add https://github.com/owner/hugo-boilerplate.git themes/boilerplate

# Update your Hugo configuration to use the theme
echo 'theme = "boilerplate"' >> hugo.toml
```

### Option 2: Manual Download

If you prefer not to use Git submodules:

```bash
# Navigate to your Hugo site's root directory
cd your-hugo-site

# Download the theme
mkdir -p themes
curl -L https://github.com/owner/hugo-boilerplate/archive/main.tar.gz | tar -xz -C themes
mv themes/hugo-boilerplate-main themes/boilerplate

# Update your Hugo configuration to use the theme
echo 'theme = "boilerplate"' >> hugo.toml
```

## Dependencies

This theme requires Node.js and npm for Tailwind CSS processing:

```bash
# Install dependencies
npm install
```

## Configuration

### Basic Configuration

Add the following to your `hugo.toml` file:

```toml
baseURL = 'https://example.com/'
languageCode = 'en-us'
title = 'Your Site Title'
theme = 'boilerplate'
defaultContentLanguage = "en"
defaultContentLanguageInSubdir = true

# Output formats configuration
[outputs]
  home = ["HTML", "RSS", "SITEMAP"]

# Site parameters
[params]
  description = "Your site description"
  author = "Your Name"
  mainSections = ["blog"]
  dateFormat = "January 2, 2006"
```

### Multilingual Setup

The theme supports multiple languages out of the box. Configure them in your `hugo.toml`:

```toml
[languages]
  [languages.en]
    languageName = "English"
    title = "English Site Title"
    weight = 1
    contentDir = "content/en"
    baseURL = "https://example.com"
    bcp47Lang = "en-us"
    [languages.en.params]
      description = "English site description"
      flag = "🇺🇸"

  [languages.de]
    languageName = "Deutsch"
    title = "Deutsche Site Title"
    weight = 2
    contentDir = "content/de"
    baseURL = "https://example.de"
    bcp47Lang = "de"
    [languages.de.params]
      description = "Deutsche Seitenbeschreibung"
      flag = "🇩🇪"
```

### Image Processing Configuration

For optimal image processing, add the following to your `hugo.toml`:

```toml
[params.imaging]
  resampleFilter = "Lanczos"
  quality = 85
  anchor = "smart"
  bgColor = "#ffffff"
  webpQuality = 85
```

## Content Structure

### Creating Blog Posts

Create a new blog post with:

```bash
hugo new content/en/blog/my-post.md
```

Front matter example:

```yaml
+++
title = 'My Post Title'
date = 2025-04-03T07:43:16+02:00
draft = false
description = "A comprehensive description for SEO purposes"
keywords = ["keyword1", "keyword2", "keyword3"]
image = "/images/blog/featured-image.jpg"
tags = ["tag1", "tag2"]
categories = ["category1"]
+++

Your post content here...
```

### Creating Glossary Terms

Create a new glossary term with:

```bash
hugo new content/en/glossary/term-name.md
```

Front matter example:

```yaml
+++
title = 'Term Name'
date = 2025-04-03T07:43:16+02:00
draft = false
url = "glossary/term-name"
description = "A comprehensive description of the term for SEO purposes"
keywords = ["keyword1", "keyword2", "keyword3"]
image = "/images/glossary/term-image.jpg"
term = "Term Name"
shortDescription = "A brief description of the term"
category = "T"
tags = ["tag1", "tag2"]
additionalImages = [
  "/images/glossary/additional-image1.jpg",
  "/images/glossary/additional-image2.jpg"
]

# CTA Section Configuration
showCTA = true
ctaHeading = "Related CTA Heading"
ctaDescription = "Call to action description text"
ctaPrimaryText = "Primary Button"
ctaPrimaryURL = "/related-url/"
ctaSecondaryText = "Secondary Button"
ctaSecondaryURL = "/another-url/"

[[faq]]
question = "Frequently asked question about the term?"
answer = "Comprehensive answer to the question that provides valuable information about the term."
+++

# What is Term Name?

Main content about the term goes here...
```

## Using Theme Components

### Shortcodes

The theme includes various shortcodes for common components:

```markdown
{{< products-with-image-grid 
  background="bg-gray-50"
  product="{ title: 'Product Title', ... }" >}}

{{< features-with-split-image
  background="bg-white"
  heading="Feature Section Heading"
  description="Feature section description text" >}}
```

### Partials

You can include partials in your templates:

```go
{{ partial "headers/centered_with_eyebrow.html" (dict 
  "eyebrow" "Eyebrow Text"
  "heading" "Main Heading"
  "description" "Description text") }}
```

## Customization

### Tailwind Configuration

The theme uses Tailwind CSS. You can customize the Tailwind configuration by editing the `tailwind.config.js` file in the theme directory.

### CSS Customization

Add custom CSS by creating a file at `assets/css/custom.css` in your project root.

### Layout Customization

Override any theme layout by creating a matching file structure in your project's `layouts` directory.

## Troubleshooting

### Common Issues

1. **PostCSS Processing Errors**: Ensure you have the correct PostCSS configuration in your project root.

2. **Image Processing Issues**: Check that Hugo has the required permissions to process images.

3. **Multilingual Configuration**: Verify that your content directories match the configured language directories.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This theme is released under the MIT license. See [LICENSE](LICENSE) for details.