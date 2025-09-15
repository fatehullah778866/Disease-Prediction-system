import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib
import os

def train_and_save_model():
    # Load dataset
    df = pd.read_csv(r'diabetes/diabetes.csv')
    
    # Replace zeros with NaN for columns where zero is not meaningful
    zero_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[zero_cols] = df[zero_cols].replace(0, np.nan)
    
    # Split data
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Handle missing values
    imputer = SimpleImputer(strategy='median')
    X = imputer.fit_transform(X)
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Create ml_model directory if it doesn't exist
    os.makedirs('diabetes/ml_model', exist_ok=True)
    
    # Save model and scaler
    with open('diabetes/ml_model/model.pkl', 'wb') as f:
        joblib.dump(model, f)
    
    with open('diabetes/ml_model/scaler.pkl', 'wb') as f:
        joblib.dump(scaler, f)
    
    # Also save imputer for future use if needed
    with open('diabetes/ml_model/imputer.pkl', 'wb') as f:
        joblib.dump(imputer, f)
    
    print("Model training complete. Model and scaler saved.")

if __name__ == "__main__":
    train_and_save_model()