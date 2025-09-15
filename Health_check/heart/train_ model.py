import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_and_save_model():
    # Load dataset
    df = pd.read_csv(r'heart/heart_disease_dataset.csv')
    
    # Drop patientid as it's not a feature
    df = df.drop('patientid', axis=1)
    
    # Handle missing values (0 in some numerical columns might indicate missing data)
    # For serumcholestrol, replace 0 with median
    df['serumcholestrol'] = df['serumcholestrol'].replace(0, df['serumcholestrol'].median())
    
    # Separate features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_scaled)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print(classification_report(y_test, y_pred))
    
    # Create ml_model directory if it doesn't exist
    os.makedirs('heart/ml_model', exist_ok=True)
    
    # Save model and scaler
    joblib.dump(model, 'heart/ml_model/model.pkl')
    joblib.dump(scaler, 'heart/ml_model/scaler.pkl')
    print("Model and scaler saved successfully!")

if __name__ == "__main__":
    train_and_save_model()