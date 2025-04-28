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

# Define image widths - can be adjusted or extended without changing the code logic
# Each width will create a resized version of the image
IMAGE_WIDTHS=(150 300 768 1024)

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
    magick identify -format "%w" "$1" 2>/dev/null || echo "0"
}

# Function to get file size in bytes
get_file_size() {
    stat -f%z "$1" 2>/dev/null || echo "0"
}

# Function to process an image
process_image() {
    local source="$1"
    local rel_path="${source#$SOURCE_DIR/}"
    local rel_dir=$(dirname "$rel_path")
    local filename=$(basename "$source")
    local extension="${filename##*.}"
    local basename="${filename%.*}"
    local is_webp=false
    
    echo "Processing: $rel_path"
    
    # Create the target directory structure that mirrors the source directory
    local target_dir="$TARGET_DIR/$rel_dir"
    mkdir -p "$target_dir"
    
    # Check if it's a WebP image
    if [[ "$extension" == "webp" ]]; then
        is_webp=true
    fi
    
    # Get original image width and size
    local original_width=$(get_image_width "$source")
    local original_size=$(get_file_size "$source")
    
    echo "  Original width: $original_width px, size: $original_size bytes"
    
    # Process each width for the image
    for width in "${IMAGE_WIDTHS[@]}"; do
        # Only process if original is larger than target width
        if [ "$original_width" -gt "$width" ]; then
            local target_file="$target_dir/${basename}-${width}.${extension}"
            
            if needs_processing "$source" "$target_file"; then
                echo "  Creating ${width}px width version in $target_dir"
                
                if [ "$is_webp" = true ]; then
                    # For WebP, just resize
                    magick "$source" -resize "${width}x>" -quality "$QUALITY_WEBP" "$target_file"
                else
                    # For other formats, create both original format and WebP
                    magick "$source" -resize "${width}x>" -quality "$QUALITY_JPG" "$target_file"
                    magick "$source" -resize "${width}x>" -quality "$QUALITY_WEBP" "$target_dir/${basename}-${width}.webp"
                fi
                
                # Check if the processed image is larger than the original
                local processed_size=$(get_file_size "$target_file")
                if [ "$processed_size" -gt "$original_size" ]; then
                    echo "  Warning: ${width}px version is larger than original, removing"
                    rm "$target_file"
                fi
            fi
        fi
    done
    
    # For non-WebP images, create a WebP version of the original
    if [ "$is_webp" = false ]; then
        local webp_target="$target_dir/${basename}.webp"
        
        if needs_processing "$source" "$webp_target"; then
            echo "  Creating WebP version of original in $target_dir"
            magick "$source" -quality "$QUALITY_WEBP" "$webp_target"
            
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
