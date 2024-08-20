FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script
COPY scripts/process_codemd.py /app/process_codemd.py
COPY entrypoint.sh /app/entrypoint.sh

# Install required packages
RUN pip install requests

# Make entrypoint.sh executable
RUN chmod +x /app/entrypoint.sh

# Command to run the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
