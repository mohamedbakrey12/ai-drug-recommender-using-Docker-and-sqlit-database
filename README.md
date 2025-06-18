

## 📄 `README.md`

````markdown
# 💊 AI Drug Recommender by using Docker and sqllite 

A Streamlit-based AI application that predicts the most appropriate drug for a patient based on input medical information. The model is trained using the `drug200.csv` dataset and leverages a Random Forest classifier.

---

## 🚀 Features

- Predicts the best drug based on patient data: Age, Sex, Blood Pressure, Cholesterol, and Sodium-to-Potassium ratio.
- Built with **Streamlit** for a modern interactive interface.
- Uses **SQLite database** to log all user inputs and prediction results.
- Fully containerized with **Docker** for consistent deployment.

---

## 🧠 Model Training

The model is trained using a Random Forest classifier on the `drug200.csv` dataset. The categorical features were encoded using `LabelEncoder`, and the trained model along with encoders were saved using `joblib`.

```bash
python train_model.py
````

---

## 🖥️ App Usage (Locally)

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

---

## 🐳 Run with Docker

> Make sure Docker is installed on your system.

### 🛠️ Build the Docker image:

```bash
docker build -t drug-app .
```

### 🚀 Run the container with volume binding:

Linux/macOS:

```bash
docker run -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none \
  drug-app
```

Windows (CMD):

```bash
docker run -p 8501:8501 -v %cd%/data:/app/data -e STREAMLIT_SERVER_FILE_WATCHER_TYPE=none drug-app
```

> All user inputs and predictions will be saved to `data/predictions.db`

---

## 📁 Project Structure

```
.
├── app.py                     # Streamlit interface
├── train_model.py             # Model training script
├── drug200.csv                # Dataset
├── *.pkl                      # Saved model and encoders
├── requirements.txt
├── Dockerfile
├── run_docker.sh / .bat       # Docker run script
├── data/                      # SQLite DB directory
└── README.md
```

---

## 📊 Example Prediction UI

* Fill in patient details
* Click “Predict Drug”
* Get result with confidence plot
* See full prediction history (optional)

---

## 📦 License

This project is for educational and research purposes.

---

## ✨ Author

Built with ❤️ by \[Mohamed Bakrey]



