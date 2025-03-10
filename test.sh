#!/bin/bash

# Base URL (Ensure it ends with a slash)
BASE_URL="http://example.com/configs/.vim/"

# Output directory
OUTPUT_DIR="./downloaded_configs"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Get the directory listing and extract links
curl -s "$BASE_URL" | grep -oP '(?<=href=")[^"]+' | while read -r file; do
    # Skip parent directory links
    if [[ "$file" != "../" && "$file" != "/" ]]; then
        FULL_URL="${BASE_URL}${file}"
        OUTPUT_FILE="${OUTPUT_DIR}/$(basename "$file")"

        echo "Checking: $FULL_URL"
        
        # Download the file if it exists
        if curl --head --silent --fail "$FULL_URL"; then
            echo "Downloading: $FULL_URL"
            curl -s -o "$OUTPUT_FILE" "$FULL_URL"
        else
            echo "File not found: $FULL_URL"
        fi
    fi
done

echo "Download process completed."
