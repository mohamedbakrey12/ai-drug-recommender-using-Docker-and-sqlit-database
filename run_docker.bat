
# For Windows users, this script builds and runs the Docker container for the drug discovery app.
@echo off
mkdir data
docker build -t drug-app .
docker run -p 8501:8501 -v %cd%/data:/app/data -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none drug-app
pause
