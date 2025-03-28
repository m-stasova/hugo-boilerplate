#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Hugo multilingual project build process..."

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "❌ Hugo is not installed. Please install Hugo first."
    exit 1
fi

# Load environment variables
if [ -f ".env" ]; then
    echo "📝 Loading environment variables..."
    source .env
else
    echo "⚠️  No .env file found. Using default configuration."
fi

# Clean public directory if it exists
if [ -d "public" ]; then
    echo "🧹 Cleaning existing public directory..."
    rm -rf public
fi

# Build for each language
echo "🏗️  Building Hugo site for all languages..."

# Function to build for a specific language
build_language() {
    local lang=$1
    local base_url=$2
    
    echo "📦 Building for $lang with base URL: $base_url"
    
    # Create language-specific environment variables
    export HUGO_BASEURL=$base_url
    
    # Build the site for this language
    hugo --minify --environment production --destination "public/$lang"
}

# Build for English
if [ ! -z "$HUGO_EN_BASEURL" ]; then
    build_language "en" "$HUGO_EN_BASEURL"
fi

# Build for German
if [ ! -z "$HUGO_DE_BASEURL" ]; then
    build_language "de" "$HUGO_DE_BASEURL"
fi

# Add more languages here as needed
# if [ ! -z "$HUGO_FR_BASEURL" ]; then
#     build_language "fr" "$HUGO_FR_BASEURL"
# fi

# Post-build checks
if [ -d "public" ]; then
    echo "✅ Build completed successfully!"
    echo "📊 Build statistics:"
    for lang in public/*; do
        if [ -d "$lang" ]; then
            lang_name=$(basename "$lang")
            echo "   $lang_name:"
            echo "   - $(find "$lang" -type f | wc -l) files generated"
            echo "   - $(du -sh "$lang" | cut -f1) total size"
        fi
    done
else
    echo "❌ Build failed - public directory was not created"
    exit 1
fi

echo "✨ Build process completed!"
