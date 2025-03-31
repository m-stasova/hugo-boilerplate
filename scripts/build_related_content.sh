#!/bin/bash
# build_related_content.sh
#
# This script creates a virtual environment, installs requirements,
# and runs the generate_related_content.py script to build related content
# YAML files for the Hugo site.

set -e  # Exit immediately if a command exits with a non-zero status

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HUGO_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Building Related Content for Hugo Site ===${NC}"
echo -e "${BLUE}Hugo root: ${HUGO_ROOT}${NC}"

# Create a virtual environment if it doesn't exist
VENV_DIR="${SCRIPT_DIR}/.venv"
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv "$VENV_DIR"
else
    echo -e "${YELLOW}Using existing virtual environment...${NC}"
fi

# Activate the virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source "${VENV_DIR}/bin/activate"

# Install or upgrade pip
echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip

# Install requirements
echo -e "${YELLOW}Installing requirements...${NC}"
pip install -r "${SCRIPT_DIR}/requirements.txt"

# Process each language directory in content/
echo -e "${YELLOW}Finding language directories...${NC}"
for lang_dir in "${HUGO_ROOT}/content/"*/; do
    # Extract language code from directory name
    lang=$(basename "$lang_dir")
    
    # Skip if not a directory or starts with underscore (like _gen)
    if [[ ! -d "$lang_dir" || "$lang" == _* ]]; then
        continue
    fi
    
    echo -e "${GREEN}Processing language: ${lang}${NC}"
    
    # Run the Python script for this language
    python "${SCRIPT_DIR}/generate_related_content.py" --lang "$lang"
done

# Deactivate the virtual environment
deactivate

echo -e "${GREEN}Done! Related content YAML files have been generated in data/related_content/${NC}"
