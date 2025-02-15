#!/bin/bash
# Run staging: read data from a file and store in temporary storage
echo "Running File Ingestion for Staging..."
python3 src/ingestion/file_ingestion.py > temp_raw.txt
# For simplicity, assume we convert the file contents to JSON and store it
python3 -c "import json; print(json.dumps({'id': 1, 'value': 100}))" > data/staging/temp_data.json
echo "Data staged."
