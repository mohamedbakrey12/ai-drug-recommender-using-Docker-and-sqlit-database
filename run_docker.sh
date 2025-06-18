#!/bin/bash FOR MACK AND LINUX
mkdir -p data
docker build -t drug-app .
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none \
  drug-app
