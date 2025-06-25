#!/bin/sh

# Check if OUTPUT_DIR is set
if [ -z "$INPUT_OUTPUT_DIR" ]; then
  echo "Output directory is not set. Please provide OUTPUT_DIR."
  exit 1
fi

# Ensure the output directory exists
mkdir -p "$INPUT_OUTPUT_DIR"

# Activate the virtual environment
if [ -f "/app/venv/bin/activate" ]; then
  . /app/venv/bin/activate
else
  echo "Virtual environment not found at /app/venv. Exiting."
  exit 1
fi

# Process all .code.md files in the repository
for file in $(find . -name '*.src.md'); do
  python /app/process_codemd.py "$file" "$INPUT_OUTPUT_DIR"
done
