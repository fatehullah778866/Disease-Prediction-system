from django.shortcuts import render
from django.http import JsonResponse
import joblib
import numpy as np
import os

# Load model and scaler once when the server starts
model_path = os.path.join(os.path.dirname(__file__), 'ml_model/model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'ml_model/scaler.pkl')

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

def predict_heart(request):
    if request.method == 'POST':
        try:
            # Get form data
            age = float(request.POST.get('age'))
            gender = int(request.POST.get('gender'))
            chest_pain = int(request.POST.get('chest_pain'))
            resting_bp = float(request.POST.get('resting_bp'))
            cholesterol = float(request.POST.get('cholesterol'))
            fasting_bs = int(request.POST.get('fasting_bs'))
            resting_ecg = int(request.POST.get('resting_ecg'))
            max_hr = float(request.POST.get('max_hr'))
            exercise_angina = int(request.POST.get('exercise_angina'))
            oldpeak = float(request.POST.get('oldpeak'))
            slope = int(request.POST.get('slope'))
            num_vessels = int(request.POST.get('num_vessels'))
            
            # Prepare features in the correct order
            features = np.array([[
                age, gender, chest_pain, resting_bp, cholesterol, fasting_bs,
                resting_ecg, max_hr, exercise_angina, oldpeak, slope, num_vessels
            ]])
            
            # Scale features
            features_scaled = scaler.transform(features)
            
            # Make prediction
            prediction = model.predict(features_scaled)
            probability = model.predict_proba(features_scaled)[0][1] * 100
            
            # Prepare result
            result = {
                'prediction': 'High Risk of Heart Disease' if prediction[0] == 1 else 'Low Risk of Heart Disease',
                'probability': round(probability, 2),
                'confidence': 'High' if probability > 70 or probability < 30 else 'Medium',
                'recommendation': 'Please consult a cardiologist immediately for further evaluation.' 
                                if prediction[0] == 1 else 'No immediate heart disease risk detected, but maintain regular checkups.',
                'input_data': {
                    'Age': age,
                    'Gender': 'Male' if gender == 1 else 'Female',
                    'Chest Pain Type': chest_pain,
                    'Resting BP': f"{resting_bp} mmHg",
                    'Cholesterol': f"{cholesterol} mg/dl",
                    'Fasting Blood Sugar': '> 120 mg/dl' if fasting_bs == 1 else '≤ 120 mg/dl',
                    'Resting ECG': resting_ecg,
                    'Max Heart Rate': max_hr,
                    'Exercise Angina': 'Yes' if exercise_angina == 1 else 'No',
                    'ST Depression': oldpeak,
                    'Slope': slope,
                    'Major Vessels': num_vessels
                }
            }
            
            return render(request, 'heart/result.html', {'result': result})
            
        except Exception as e:
            return render(request, 'heart/predict.html', {'error': f"An error occurred: {str(e)}"})
    
    return render(request, 'heart/predict.html')

def heart_home(request):
    return render(request, 'heart/predict.html')


def heart_detail(request):
    return render(request, 'heart/details.html')
