#!/bin/bash

# Image processing script for Hugo
# This script prepares the image directory structure for Hugo
# Hugo's built-in image processing will handle resizing and format conversion
# during the build process via the lazyimg.html partial

# Get the root directory of the Hugo site
SITE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../" && pwd)"

echo "Preparing image directories for Hugo processing..."

# Ensure the static/images directory exists
mkdir -p "$SITE_ROOT/static/images"

# No need to pre-process images as Hugo will handle this during build
# Just ensure all images are properly placed in static/images

# Check if we're in a CI environment (like Cloudflare Pages or Amplify)
if [ -n "$CI" ] || [ -n "$CLOUDFLARE_PAGES" ] || [ -n "$AWS_AMPLIFY" ]; then
  echo "CI environment detected. Skipping external image processing."
  echo "Hugo will handle image processing during build time."
else
  echo "Local environment detected."
  echo "Images in static/images will be processed by Hugo during build time."
  
  # Count the number of images in the static/images directory
  IMAGE_COUNT=$(find "$SITE_ROOT/static/images/" -type f -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.webp" -o -name "*.gif" | wc -l)
  echo "Found $IMAGE_COUNT images in static/images directory."
  
  # Remind about Hugo's image processing
  echo ""
  echo "IMPORTANT: Image processing is now handled by Hugo's built-in capabilities."
  echo "The lazyimg.html partial will automatically:"
  echo "  - Create responsive image sizes"
  echo "  - Generate WebP versions"
  echo "  - Apply lazy loading"
  echo "  - Set appropriate image attributes"
  echo ""
  echo "No external tools like ImageMagick are required."
fi

echo "Image preparation complete!"
