

## 📄 ملف: `DOCKER_GUIDE.md`

````markdown
# 🐳 Docker Usage Guide for AI Drug Recommender App

This file documents all the Docker-related commands and configurations used in this project—from basics to advanced usage with volumes and environment variables.

---

## 🛠️ 1. Dockerfile

Used to containerize the Streamlit application.

```Dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
````

---

## 🏗️ 2. Build Docker Image

Build the image with a custom tag (e.g., `drug-app`):

```bash
docker build -t drug-app .
```

---

## 🚀 3. Run Container (Basic)

Run the container and map port 8501:

```bash
docker run -p 8501:8501 drug-app
```

Access the app at:
`http://localhost:8501`

---

## 💾 4. Run with Volume (Persistent Database)

To persist the SQLite database across runs, use a **volume** that maps a local `data/` directory to `/app/data` in the container.

### For macOS/Linux:

```bash
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none \
  drug-app
```

### For Windows (CMD):

```bash
docker run -p 8501:8501 -v %cd%/data:/app/data -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none drug-app
```

### For Windows (PowerShell):

```powershell
docker run -p 8501:8501 `
  -v ${PWD}/data:/app/data `
  -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none `
  drug-app
```

> `STREAMLIT_SERVER_FILE_WATCHER_TYPE=none` is used to fix file-watching issues inside Docker.

---

## 📂 5. Bind Mount Summary

| Host Path | Container Path | Purpose                 |
| --------- | -------------- | ----------------------- |
| `./data`  | `/app/data`    | Stores `predictions.db` |

---

## 🧼 6. Clean Up Docker

Remove all stopped containers:

```bash
docker container prune
```

Remove the image:

```bash
docker rmi drug-app
```

---

## 📝 7. File Watcher Note

In development mode, use this environment variable to prevent Streamlit from reloading:

```bash
-e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none
```

---

## 📌 Tips

* Always build again after code changes: `docker build -t drug-app .`
* Use volumes to persist data.
* Consider using `docker-compose` for multi-container setups (e.g., with PostgreSQL or API backend).

---

## ✅ Sample Full Run Script (run\_docker.sh)

```bash
#!/bin/bash
mkdir -p data
docker build -t drug-app .
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none \
  drug-app


