#!/bin/bash

# Image preprocessing script for Wachman
# This script preprocesses images and stores them in the static/images/processed directory
# Images are only processed if they are larger than the size limits
# For WebP images, only size alternatives are created, no format conversion
# If the processed image is larger than the original, it is not used

# Set error handling
set -e

# Get the root directory of the Hugo site
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
THEME_DIR="$(dirname "$SCRIPT_DIR")"
HUGO_ROOT="$(dirname "$(dirname "$THEME_DIR")")"

SOURCE_DIR="$HUGO_ROOT/static/images"
TARGET_DIR="$HUGO_ROOT/static/images/processed"

# Create the processed directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Define image sizes
SMALL_WIDTH=150
MEDIUM_WIDTH=300
LARGE_WIDTH=1024

# Quality settings
QUALITY_JPG=85
QUALITY_WEBP=85

# Function to check if the file exists and is newer than the target
needs_processing() {
    local source="$1"
    local target="$2"
    
    # If target doesn't exist, we need to process
    if [ ! -f "$target" ]; then
        return 0 # true
    fi
    
    # If source is newer than target, we need to process
    if [ "$source" -nt "$target" ]; then
        return 0 # true
    fi
    
    return 1 # false
}

# Function to get image dimensions using identify from ImageMagick
get_image_width() {
    identify -format "%w" "$1" 2>/dev/null || echo "0"
}

# Function to get file size in bytes
get_file_size() {
    stat -f%z "$1" 2>/dev/null || echo "0"
}

# Function to process an image
process_image() {
    local source="$1"
    local filename=$(basename "$source")
    local extension="${filename##*.}"
    local basename="${filename%.*}"
    local is_webp=false
    
    echo "Processing: $filename"
    
    # Check if it's a WebP image
    if [[ "$extension" == "webp" ]]; then
        is_webp=true
    fi
    
    # Get original image width and size
    local original_width=$(get_image_width "$source")
    local original_size=$(get_file_size "$source")
    
    echo "  Original width: $original_width px, size: $original_size bytes"
    
    # Process small size if original is larger
    if [ "$original_width" -gt "$SMALL_WIDTH" ]; then
        local small_target="$TARGET_DIR/${basename}-${SMALL_WIDTH}.${extension}"
        
        if needs_processing "$source" "$small_target"; then
            echo "  Creating small size ($SMALL_WIDTH px)"
            
            if [ "$is_webp" = true ]; then
                # For WebP, just resize
                convert "$source" -resize "${SMALL_WIDTH}x" -quality "$QUALITY_WEBP" "$small_target"
            else
                # For other formats, create both original format and WebP
                convert "$source" -resize "${SMALL_WIDTH}x" -quality "$QUALITY_JPG" "$small_target"
                convert "$source" -resize "${SMALL_WIDTH}x" -quality "$QUALITY_WEBP" "$TARGET_DIR/${basename}-${SMALL_WIDTH}.webp"
            fi
            
            # Check if the processed image is larger than the original
            local processed_size=$(get_file_size "$small_target")
            if [ "$processed_size" -gt "$original_size" ]; then
                echo "  Warning: Small size is larger than original, removing"
                rm "$small_target"
            fi
        fi
    fi
    
    # Process medium size if original is larger
    if [ "$original_width" -gt "$MEDIUM_WIDTH" ]; then
        local medium_target="$TARGET_DIR/${basename}-${MEDIUM_WIDTH}.${extension}"
        
        if needs_processing "$source" "$medium_target"; then
            echo "  Creating medium size ($MEDIUM_WIDTH px)"
            
            if [ "$is_webp" = true ]; then
                # For WebP, just resize
                convert "$source" -resize "${MEDIUM_WIDTH}x" -quality "$QUALITY_WEBP" "$medium_target"
            else
                # For other formats, create both original format and WebP
                convert "$source" -resize "${MEDIUM_WIDTH}x" -quality "$QUALITY_JPG" "$medium_target"
                convert "$source" -resize "${MEDIUM_WIDTH}x" -quality "$QUALITY_WEBP" "$TARGET_DIR/${basename}-${MEDIUM_WIDTH}.webp"
            fi
            
            # Check if the processed image is larger than the original
            local processed_size=$(get_file_size "$medium_target")
            if [ "$processed_size" -gt "$original_size" ]; then
                echo "  Warning: Medium size is larger than original, removing"
                rm "$medium_target"
            fi
        fi
    fi
    
    # Process large size if original is larger
    if [ "$original_width" -gt "$LARGE_WIDTH" ]; then
        local large_target="$TARGET_DIR/${basename}-${LARGE_WIDTH}.${extension}"
        
        if needs_processing "$source" "$large_target"; then
            echo "  Creating large size ($LARGE_WIDTH px)"
            
            if [ "$is_webp" = true ]; then
                # For WebP, just resize
                convert "$source" -resize "${LARGE_WIDTH}x" -quality "$QUALITY_WEBP" "$large_target"
            else
                # For other formats, create both original format and WebP
                convert "$source" -resize "${LARGE_WIDTH}x" -quality "$QUALITY_JPG" "$large_target"
                convert "$source" -resize "${LARGE_WIDTH}x" -quality "$QUALITY_WEBP" "$TARGET_DIR/${basename}-${LARGE_WIDTH}.webp"
            fi
            
            # Check if the processed image is larger than the original
            local processed_size=$(get_file_size "$large_target")
            if [ "$processed_size" -gt "$original_size" ]; then
                echo "  Warning: Large size is larger than original, removing"
                rm "$large_target"
            fi
        fi
    fi
    
    # For non-WebP images, create a WebP version of the original
    if [ "$is_webp" = false ]; then
        local webp_target="$TARGET_DIR/${basename}.webp"
        
        if needs_processing "$source" "$webp_target"; then
            echo "  Creating WebP version"
            convert "$source" -quality "$QUALITY_WEBP" "$webp_target"
            
            # Check if the processed image is larger than the original
            local processed_size=$(get_file_size "$webp_target")
            if [ "$processed_size" -gt "$original_size" ]; then
                echo "  Warning: WebP version is larger than original, removing"
                rm "$webp_target"
            fi
        fi
    fi
}

# Main function to process all images
process_all_images() {
    # Find all images in the source directory
    echo "Finding images in $SOURCE_DIR..."
    image_count=0

    find "$SOURCE_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.webp" \) -not -path "*/processed/*" | while read -r image; do
        process_image "$image"
        image_count=$((image_count + 1))
    done

    echo "Processed $image_count images"
    echo "Image preprocessing complete!"
}

# If script is run directly, process all images
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    process_all_images
fi
