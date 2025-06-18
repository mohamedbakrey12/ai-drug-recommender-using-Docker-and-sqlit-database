import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime



# تحميل النموذج والمحولات
model = joblib.load("pkl\drug_prediction_model.pkl")
le_sex = joblib.load("pkl\le_sex.pkl")
le_bp = joblib.load("pkl\le_bp.pkl")
le_chol = joblib.load("pkl\pklle_chol.pkl")
le_drug = joblib.load("pkl\le_drug.pkl")


def create_db():
    conn = sqlite3.connect("data/predictions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            sex TEXT,
            bp TEXT,
            cholesterol TEXT,
            na_to_k REAL,
            predicted_drug TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_prediction(age, sex, bp, cholesterol, na_to_k, predicted_drug):
    conn = sqlite3.connect("data/predictions.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predictions (age, sex, bp, cholesterol, na_to_k, predicted_drug)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (age, sex, bp, cholesterol, na_to_k, predicted_drug))
    conn.commit()
    conn.close()





# إنشاء القاعدة عند التشغيل
create_db()

# واجهة التطبيق
st.title("💊 نظام ذكي لتوقع الدواء المناسب")
st.markdown("📋 أدخل بيانات المريض التالية:")

# إدخال بيانات المستخدم
age = st.number_input("📅 العمر", min_value=1, max_value=120, value=30)
sex = st.selectbox("🧍 الجنس", le_sex.classes_)
bp = st.selectbox("🩸 ضغط الدم", le_bp.classes_)
chol = st.selectbox("🧪 الكوليسترول", le_chol.classes_)
na_to_k = st.number_input("⚖️ نسبة الصوديوم إلى البوتاسيوم (Na_to_K)", min_value=0.0, max_value=50.0, value=15.0)

# تجهيز البيانات
input_data = np.array([[age,
                        le_sex.transform([sex])[0],
                        le_bp.transform([bp])[0],
                        le_chol.transform([chol])[0],
                        na_to_k]])

# التنبؤ
if st.button("🔍 توقع الدواء"):
    prediction = model.predict(input_data)[0]
    prediction_label = le_drug.inverse_transform([prediction])[0]

    # حفظ البيانات في قاعدة البيانات
    save_prediction(age, sex, bp, chol, na_to_k, prediction_label)

    # عرض النتيجة
    st.success(f"🧠 Model predict **{prediction_label}**")

    # رسم احتمالات
    probabilities = model.predict_proba(input_data)[0]
    class_labels = le_drug.inverse_transform(np.arange(len(probabilities)))

    fig, ax = plt.subplots()
    bars = ax.bar(class_labels, probabilities, color="skyblue")
    ax.set_ylabel("Probability")
    ax.set_title("Accuracy of Drug Prediction")
    ax.set_ylim(0, 1)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9)

    st.pyplot(fig)




def save_prediction(age, sex, bp, cholesterol, na_to_k, predicted_drug):
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO predictions (age, sex, bp, cholesterol, na_to_k, predicted_drug)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (age, sex, bp, cholesterol, na_to_k, predicted_drug))
    conn.commit()
    conn.close()
