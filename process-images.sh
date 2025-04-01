#!/bin/bash

# Image processing script for Hugo
# This script processes all images in the static/images directory
# and creates multiple sizes and formats for responsive image loading

# Configuration
SMALL_WIDTH=150
MEDIUM_WIDTH=300
LARGE_WIDTH=1024
QUALITY_ORIG=85
QUALITY_WEBP=85

# Get list of language directories
LANG_DIRS=()
for dir in public/*; do
  if [ -d "$dir" ] && [ "$(basename "$dir")" != "images" ]; then
    LANG_DIRS+=("$dir")
  fi
done

# Add the default language directory (public) to the list
LANG_DIRS+=("public")

# Ensure the public/images directory exists
mkdir -p public/images

# Process all images in the static/images directory
for IMAGE in static/images/*; do
  # Skip if not a file
  if [ ! -f "$IMAGE" ]; then
    continue
  fi
  
  # Get file extension and name
  FILENAME=$(basename "$IMAGE")
  
  # Handle the special case of double extension (e.g., rag-vs-cag-950x950.jpg.webp)
  if [[ "$FILENAME" == *".jpg.webp" ]]; then
    # For this special case, treat it as a WebP file but also generate JPG versions
    EXTENSION="webp"
    FILENAME_WITHOUT_EXT="${FILENAME%.webp}"
    FILENAME_WITHOUT_BOTH="${FILENAME%.jpg.webp}"
    IS_SPECIAL_CASE=true
  else
    # Normal case
    EXTENSION="${FILENAME##*.}"
    FILENAME_WITHOUT_EXT="${FILENAME%.*}"
    IS_SPECIAL_CASE=false
  fi
  
  # Skip if not an image
  if [[ ! "$EXTENSION" =~ ^(jpg|jpeg|png|webp|gif)$ ]]; then
    continue
  fi
  
  echo "Processing $FILENAME..."
  
  # Check if it's a WebP image
  IS_WEBP=false
  if [ "$EXTENSION" = "webp" ]; then
    IS_WEBP=true
  fi
  
  # Get image dimensions
  WIDTH=$(magick identify -format "%w" "$IMAGE")
  
  # Generate small size
  if [ "$WIDTH" -gt "$SMALL_WIDTH" ]; then
    # Original format
    echo "  Creating small size ($SMALL_WIDTH px)..."
    if [ "$IS_SPECIAL_CASE" = true ]; then
      # For special case, create both WebP and JPG
      magick "$IMAGE" -resize ${SMALL_WIDTH}x -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_BOTH}-${SMALL_WIDTH}.webp"
      magick "$IMAGE" -resize ${SMALL_WIDTH}x -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_BOTH}-${SMALL_WIDTH}.jpg"
    else
      # Normal case
      magick "$IMAGE" -resize ${SMALL_WIDTH}x -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_EXT}-${SMALL_WIDTH}.${EXTENSION}"
      
      # WebP format (if not already WebP)
      if [ "$IS_WEBP" = false ]; then
        echo "  Creating small WebP ($SMALL_WIDTH px)..."
        magick "$IMAGE" -resize ${SMALL_WIDTH}x -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_EXT}-${SMALL_WIDTH}.webp"
      fi
    fi
  fi
  
  # Generate medium size
  if [ "$WIDTH" -gt "$MEDIUM_WIDTH" ]; then
    # Original format
    echo "  Creating medium size ($MEDIUM_WIDTH px)..."
    if [ "$IS_SPECIAL_CASE" = true ]; then
      # For special case, create both WebP and JPG
      magick "$IMAGE" -resize ${MEDIUM_WIDTH}x -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_BOTH}-${MEDIUM_WIDTH}.webp"
      magick "$IMAGE" -resize ${MEDIUM_WIDTH}x -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_BOTH}-${MEDIUM_WIDTH}.jpg"
    else
      # Normal case
      magick "$IMAGE" -resize ${MEDIUM_WIDTH}x -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_EXT}-${MEDIUM_WIDTH}.${EXTENSION}"
      
      # WebP format (if not already WebP)
      if [ "$IS_WEBP" = false ]; then
        echo "  Creating medium WebP ($MEDIUM_WIDTH px)..."
        magick "$IMAGE" -resize ${MEDIUM_WIDTH}x -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_EXT}-${MEDIUM_WIDTH}.webp"
      fi
    fi
  fi
  
  # Generate large size
  if [ "$WIDTH" -gt "$LARGE_WIDTH" ]; then
    # Original format
    echo "  Creating large size ($LARGE_WIDTH px)..."
    if [ "$IS_SPECIAL_CASE" = true ]; then
      # For special case, create both WebP and JPG
      magick "$IMAGE" -resize ${LARGE_WIDTH}x -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_BOTH}-${LARGE_WIDTH}.webp"
      magick "$IMAGE" -resize ${LARGE_WIDTH}x -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_BOTH}-${LARGE_WIDTH}.jpg"
    else
      # Normal case
      magick "$IMAGE" -resize ${LARGE_WIDTH}x -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_EXT}-${LARGE_WIDTH}.${EXTENSION}"
      
      # WebP format (if not already WebP)
      if [ "$IS_WEBP" = false ]; then
        echo "  Creating large WebP ($LARGE_WIDTH px)..."
        magick "$IMAGE" -resize ${LARGE_WIDTH}x -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_EXT}-${LARGE_WIDTH}.webp"
      fi
    fi
  fi
  
  # Always generate original formats if special case
  if [ "$IS_SPECIAL_CASE" = true ]; then
    echo "  Creating original JPG version..."
    magick "$IMAGE" -quality $QUALITY_ORIG "public/images/${FILENAME_WITHOUT_BOTH}.jpg"
  fi
  
  # Always generate WebP version of original if not already WebP
  if [ "$IS_WEBP" = false ]; then
    echo "  Creating WebP version of original..."
    magick "$IMAGE" -quality $QUALITY_WEBP "public/images/${FILENAME_WITHOUT_EXT}.webp"
  fi
  
  # Copy the original image to public directory
  echo "  Copying original image..."
  cp "$IMAGE" "public/images/$FILENAME"
done

# Copy all processed images to each language directory
echo "Copying processed images to language directories..."
for LANG_DIR in "${LANG_DIRS[@]}"; do
  if [ "$LANG_DIR" != "public" ]; then
    echo "  Copying to $LANG_DIR/images..."
    mkdir -p "$LANG_DIR/images"
    cp -r public/images/* "$LANG_DIR/images/"
  fi
done

echo "Image processing complete!"
