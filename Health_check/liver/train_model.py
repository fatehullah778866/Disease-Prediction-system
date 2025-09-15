import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_and_save_model():
    # Load dataset
    df = pd.read_csv(r'liver/liver_disease_dataset.csv')
    
    # Handle missing values (one row has missing A/G Ratio)
    df['Albumin_and_Globulin_Ratio'].fillna(
        df['Albumin_and_Globulin_Ratio'].median(), inplace=True)
    
    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    # Feature scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        random_state=42
    )
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Create ml_model directory if it doesn't exist
    os.makedirs('liver/ml_model', exist_ok=True)
    
    # Save model and scaler
    joblib.dump(model, 'liver/ml_model/model.pkl')
    joblib.dump(scaler, 'liver/ml_model/scaler.pkl')
    print("Model and scaler saved successfully!")

if __name__ == "__main__":
    train_and_save_model()