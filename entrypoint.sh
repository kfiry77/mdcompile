#!/bin/sh

# Check if OUTPUT_DIR is set
if [ -z "$INPUT_OUTPUT_DIR" ]; then
  echo "Output directory is not set. Please provide OUTPUT_DIR."
  exit 1
fi

# Ensure the output directory exists
mkdir -p "$INPUT_OUTPUT_DIR"

# Process all .code.md files in the repository
for file in $(find . -name '*.src.md'); do
  python /app/process_codemd.py "$file" "$INPUT_OUTPUT_DIR"
done

