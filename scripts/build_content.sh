#!/bin/bash
# build_content.sh
#
# This script creates a virtual environment, installs requirements,
# and performs three main tasks:
# 1. Translates missing content files from English to other languages using FlowHunt API
# 2. Generates related content YAML files for the Hugo site
# 3. Preprocesses images for optimal web delivery

set -e  # Exit immediately if a command exits with a non-zero status

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
THEME_DIR="$(dirname "$SCRIPT_DIR")"
HUGO_ROOT="$(dirname "$(dirname "$THEME_DIR")")"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color



#print directories
echo -e "${BLUE}=== Directories ===${NC}"
echo -e "${BLUE}Script directory: ${SCRIPT_DIR}${NC}"
echo -e "${BLUE}Theme directory: ${THEME_DIR}${NC}"
echo -e "${BLUE}Hugo root: ${HUGO_ROOT}${NC}"

echo -e "${BLUE}=== Building Content for Hugo Site ===${NC}"
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

# Check for FlowHunt API key
if [ -z "$FLOWHUNT_API_KEY" ]; then
    echo -e "${YELLOW}Checking for FlowHunt API key...${NC}"
    if [ ! -f "${SCRIPT_DIR}/.env" ]; then
        echo -e "${YELLOW}No .env file found. Please enter your FlowHunt API key:${NC}"
        read -p "FlowHunt API Key: " flow_api_key
        echo "FLOWHUNT_API_KEY=${flow_api_key}" >> "${SCRIPT_DIR}/.env"
    elif ! grep -q "FLOWHUNT_API_KEY" "${SCRIPT_DIR}/.env"; then
        echo -e "${YELLOW}FlowHunt API key not found in .env file. Please enter your FlowHunt API key:${NC}"
        read -p "FlowHunt API Key: " flow_api_key
        echo "FLOWHUNT_API_KEY=${flow_api_key}" >> "${SCRIPT_DIR}/.env"
    fi
fi

# STEP 0 validate if all content file are in the correct format with script validate_content.sh
echo -e "${BLUE}=== Step 0: Validating Content Files ===${NC}"

bash "${SCRIPT_DIR}/validate_content.sh" --path "${HUGO_ROOT}/content"
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}Content file validation failed. Stopping further processing.${NC}"
    exit 1
fi
echo -e "${GREEN}Content file validation completed!${NC}"



# STEP 1: Run the translation script with FlowHunt
echo -e "${BLUE}=== Step 1: Translating Missing Content with FlowHunt API ===${NC}"
echo -e "${YELLOW}Running FlowHunt translation script...${NC}"
python "${SCRIPT_DIR}/translate_with_flowhunt.py" --path "${HUGO_ROOT}/content"
echo -e "${GREEN}Translation of missing content completed!${NC}"

# STEP 1.5: Validate the content files again after translation
echo -e "${BLUE}=== Step 1.5: Validating Content Files after translation ===${NC}"
python "${SCRIPT_DIR}/sync_content_attributes.py"
echo -e "${GREEN}Content attributes sync completed!${NC}"

# after translation validate again
echo -e "${BLUE}=== Step 1.6: Validating Content Files after translation ===${NC}"

bash "${SCRIPT_DIR}/validate_content.sh" --path "${HUGO_ROOT}/content"
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}Content file validation failed. Stopping further processing.${NC}"
    exit 1
fi
echo -e "${GREEN}Content file validation completed!${NC}"




# STEP 2: Generate Related Content
echo -e "${BLUE}=== Step 2: Generating Related Content ===${NC}"
python "${SCRIPT_DIR}/generate_related_content.py" --path "${HUGO_ROOT}/content" --hugo-root "${HUGO_ROOT}"
echo -e "${GREEN}Related content generation completed!${NC}"

# STEP 3: Preprocess Images
echo -e "${BLUE}=== Step 3: Preprocessing Images ===${NC}"
echo -e "${YELLOW}Running image preprocessing script...${NC}"
# Source the preprocess-images.sh script to use its functions
source "${SCRIPT_DIR}/preprocess-images.sh"
# Run the image preprocessing
process_all_images
echo -e "${GREEN}Image preprocessing completed!${NC}"

# Deactivate the virtual environment
deactivate


echo -e "${GREEN}Done! All content processing completed successfully.${NC}"
