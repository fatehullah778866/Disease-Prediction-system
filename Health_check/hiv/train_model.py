import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

def train_hiv_model():
    # Load the dataset
    df = pd.read_csv(r'hiv/HIV_AIDS_Balanced_1000.csv')
    
    # Data Exploration
    print("Dataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDescriptive Statistics:")
    print(df.describe())
    
    # Feature Engineering
    # Create age groups
    df['age_group'] = pd.cut(df['age'], bins=[0, 20, 30, 40, 50, 60, 70, 100], 
                            labels=['0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70+'])
    
    # Create BMI from weight (assuming height is average)
    # Note: This is a simplification - real implementation would need actual height
    df['bmi'] = df['wtkg'] / ((1.7) ** 2)
    
    # Feature Selection
    # Dropping columns that are not useful or redundant
    features = ['age', 'wtkg', 'hemo', 'homo', 'drugs', 'karnof', 'cd40', 'cd420', 'cd80', 'cd820', 'bmi']
    target = 'infected'
    
    X = df[features]
    y = df[target]
    
    # Handle missing values if any
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
    os.makedirs('hiv/ml_model', exist_ok=True)
    joblib.dump(model, 'hiv/ml_model/model.pkl')
    joblib.dump(scaler, 'hiv/ml_model/scaler.pkl')
    print("\nModel and scaler saved successfully!")

if __name__ == "__main__":
    train_hiv_model()