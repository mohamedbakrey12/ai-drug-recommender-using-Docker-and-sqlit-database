import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# تحميل البيانات
df = pd.read_csv("dtataset\drug200.csv")

# ترميز البيانات الفئوية
le_sex = LabelEncoder()
le_bp = LabelEncoder()
le_chol = LabelEncoder()
le_drug = LabelEncoder()

df["Sex"] = le_sex.fit_transform(df["Sex"])
df["BP"] = le_bp.fit_transform(df["BP"])
df["Cholesterol"] = le_chol.fit_transform(df["Cholesterol"])
df["Drug"] = le_drug.fit_transform(df["Drug"])

# حفظ المحولات للاستخدام لاحقًا
joblib.dump(le_sex, "le_sex.pkl")
joblib.dump(le_bp, "le_bp.pkl")
joblib.dump(le_chol, "le_chol.pkl")
joblib.dump(le_drug, "le_drug.pkl")

# تقسيم البيانات
X = df.drop("Drug", axis=1)
y = df["Drug"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تدريب النموذج
model = RandomForestClassifier()
model.fit(X_train, y_train)

# تقييم النموذج
print(classification_report(y_test, model.predict(X_test)))

# حفظ النموذج
joblib.dump(model, "drug_prediction_model.pkl")
