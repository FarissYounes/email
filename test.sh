#!/bin/bash

# Base URL
BASE_URL="http://example.com/configs/.vim/"

# Output directory
OUTPUT_DIR="./downloaded_configs"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Generate common file names (modify as needed)
POSSIBLE_FILES=(
    "vimrc"
    "init.vim"
    "plugins.vim"
    "colorscheme.vim"
    ".vimrc"
    "config.json"
    "settings.yml"
)

# Try each file
for file in "${POSSIBLE_FILES[@]}"; do
    FULL_URL="${BASE_URL}${file}"
    OUTPUT_FILE="${OUTPUT_DIR}/${file}"

    echo "Checking: $FULL_URL"

    if curl --head --silent --fail "$FULL_URL"; then
        echo "Downloading: $FULL_URL"
        curl -s -o "$OUTPUT_FILE" "$FULL_URL"
    else
        echo "File not found: $FULL_URL"
    fi
done

echo "Download process completed."
