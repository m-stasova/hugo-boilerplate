#!/bin/bash

# Directory containing the markdown files
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CONTENT_DIR="$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")/content"

# Print content directory
echo "Content directory: $CONTENT_DIR"

# Check if the content directory exists
if [ ! -d "$CONTENT_DIR" ]; then
    echo "Error: Content directory does not exist at $CONTENT_DIR"
    exit 1
fi

# Clean up any existing temporary files first
echo "Cleaning up any existing temporary files..."
find "$CONTENT_DIR" -name "*.md.tmp" -type f -delete

# Default date value
DEFAULT_DATE="$(date +"%Y-%m-%d %H:%M:%S")"

# First, count the number of .md files
FILE_COUNT=$(find "$CONTENT_DIR" -type f -name "*.md" | wc -l)
echo "Found $FILE_COUNT Markdown files to process"

# Use find to recursively locate all .md files in the content directory and subdirectories
find "$CONTENT_DIR" -type f -name "*.md" | while read -r file; do
    # Debug: print file being processed
    echo "Processing: $file"
    
    # Check if file has frontmatter and is missing the date parameter
    if grep -q "^---\|^\+++" "$file" && ! grep -q "^date:" "$file"; then
        echo "  Found file with missing date: $file"
        
        # Determine frontmatter delimiter (--- or +++)
        delimiter=$(grep -m1 "^---\|^\+++" "$file" | head -n1)
        
        # Create a temp file
        tmp_file="${file}.tmp"
        
        # Add the date parameter to the beginning of the frontmatter
        if awk -v date="date: $DEFAULT_DATE" -v dlm="$delimiter" '
            BEGIN { added = 0 }
            $0 ~ dlm && !added { print; print date; added = 1; next }
            { print }
        ' "$file" > "$tmp_file"; then
            # Only replace original if the temp file was created successfully
            mv "$tmp_file" "$file"
            echo "  Added missing date to $file"
        else
            echo "  Error processing $file"
            # Clean up the temp file if it exists but there was an error
            [ -f "$tmp_file" ] && rm "$tmp_file"
        fi
    fi
done

# Final cleanup to ensure no temporary files are left
find "$CONTENT_DIR" -name "*.md.tmp" -type f -delete

echo "Finished processing all files."