#!/bin/bash

# Directory containing the markdown files
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CONTENT_DIR="$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")/content"

# Find all .md files in the content directory and its subdirectories
find "$CONTENT_DIR" -type f -name "*.md" | while read -r file; do
    # Read the first line of the file
    first_line=$(head -n 1 "$file")
    
    # Trim whitespace and check if the first line is exactly "+++"
    trimmed_line=$(echo "$first_line" | tr -d '[:space:]')
    if [[ "$trimmed_line" != "+++" ]]; then
        echo -e "Validation failed: $file does not start with +++"
        echo -e "First line content: '$trimmed_line'"
    fi
done