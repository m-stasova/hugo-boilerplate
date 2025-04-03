#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Get the Hugo root directory
HUGO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

echo "=== Building Content ==="
"$SCRIPT_DIR/build_content.sh"

echo "=== Building Hugo site ==="
cd "$HUGO_ROOT" && hugo --gc --minify -e production

echo "=== Processing images ==="
"$SCRIPT_DIR/process-images.sh"

cd "$HUGO_ROOT" && hugo server