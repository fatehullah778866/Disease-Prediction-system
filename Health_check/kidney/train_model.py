import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

def train_ckd_model():
    # Load the dataset
    df = pd.read_csv(r'kidney/Chronic_Kidney_Dsease_data.csv')
    
    # Data Exploration
    print("Dataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDescriptive Statistics:")
    print(df.describe())
    
    # Feature Selection
    features = [
        'Age', 'BMI', 'SystolicBP', 'DiastolicBP', 'FastingBloodSugar', 'HbA1c', 
        'SerumCreatinine', 'BUNLevels', 'GFR', 'ProteinInUrine', 'ACR', 
        'HemoglobinLevels', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL', 
        'CholesterolTriglycerides', 'FamilyHistoryKidneyDisease', 
        'FamilyHistoryHypertension', 'FamilyHistoryDiabetes', 
        'PreviousAcuteKidneyInjury', 'UrinaryTractInfections', 'Edema', 
        'FatigueLevels', 'NauseaVomiting', 'MuscleCramps', 'Itching'
    ]
    target = 'Diagnosis'
    
    X = df[features]
    y = df[target]
    
    # Handle missing values
    X.fillna(X.mean(), inplace=True)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Model Training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Model Evaluation
    y_pred = model.predict(X_test_scaled)
    
    print("\nModel Evaluation:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Feature Importance
    print("\nFeature Importances:")
    for feature, importance in zip(features, model.feature_importances_):
        print(f"{feature}: {importance:.4f}")
    
    # Save model and scaler
    os.makedirs('kidney/ml_model', exist_ok=True)
    joblib.dump(model, 'kidney/ml_model/model.pkl')
    joblib.dump(scaler, 'kidney/ml_model/scaler.pkl')
    print("\nModel and scaler saved successfully!")

if __name__ == "__main__":
    train_ckd_model()