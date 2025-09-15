import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'breast-cancer.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model', 'model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'ml_model', 'scaler.pkl')

# Load and preprocess data
def load_and_preprocess_data():
    # Read the dataset
    df = pd.read_csv(DATA_PATH)
    
    # Drop ID column as it's not a feature
    df = df.drop('id', axis=1)
    
    # Encode diagnosis (M=1, B=0)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
    
    # Check for missing values
    if df.isnull().sum().sum() > 0:
        df = df.fillna(df.mean())  # Impute missing values with mean
    
    # Features and target
    X = df.drop('diagnosis', axis=1)
    y = df['diagnosis']
    
    return X, y

# Train model and save
def train_and_save_model():
    # Ensure ml_model directory exists
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    
    # Load data
    X, y = load_and_preprocess_data()
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Save model and scaler
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
    print(f"Model saved to {MODEL_PATH}")
    print(f"Scaler saved to {SCALER_PATH}")

if __name__ == "__main__":
    train_and_save_model()