#!/bin/bash

echo "=== Building Hugo site ==="
hugo --gc --minify -e production

echo "=== Processing images ==="
./process-images.sh

hugo server