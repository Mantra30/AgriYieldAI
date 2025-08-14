import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib
import os

# Load data
data = pd.read_csv("crop_data.csv")

# Define features
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Encode crop labels
label_encoder = LabelEncoder()
data['label_encoded'] = label_encoder.fit_transform(data['label'])

# Classification model (crop name)
X_cls = data[features]
y_cls = data['label_encoded']
X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)
cls_model = RandomForestClassifier()
cls_model.fit(X_train_cls, y_train_cls)

# Save classification model and encoder
os.makedirs('model', exist_ok=True)
joblib.dump(cls_model, 'model/classifier_model.pkl')
joblib.dump(label_encoder, 'model/label_encoder.pkl')

# Regression model (yield)
y_reg = data['yield_kg_per_hectare']
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_cls, y_reg, test_size=0.2, random_state=42)
reg_model = RandomForestRegressor()
reg_model.fit(X_train_reg, y_train_reg)
joblib.dump(reg_model, 'model/yield_model.pkl')

print("✅ Both models trained and saved successfully.")
