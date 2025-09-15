from django.shortcuts import render, redirect
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

def predict_hiv(request):
    if request.method == 'POST':
        try:
            # Get form data
            age = float(request.POST.get('age'))
            wtkg = float(request.POST.get('weight'))
            hemo = int(request.POST.get('hemo'))
            homo = int(request.POST.get('homo'))
            drugs = int(request.POST.get('drugs'))
            karnof = int(request.POST.get('karnof'))
            cd40 = float(request.POST.get('cd40'))
            cd420 = float(request.POST.get('cd420'))
            cd80 = float(request.POST.get('cd80'))
            cd820 = float(request.POST.get('cd820'))
            
            # Calculate BMI (simplified)
            bmi = wtkg / ((1.7) ** 2)
            
            # Prepare features
            features = np.array([[age, wtkg, hemo, homo, drugs, karnof, cd40, cd420, cd80, cd820, bmi]])
            
            # Scale features
            features_scaled = scaler.transform(features)
            
            # Make prediction
            prediction = model.predict(features_scaled)
            probability = model.predict_proba(features_scaled)[0][1] * 100
            
            # Prepare result
            result = {
                'prediction': 'Positive' if prediction[0] == 1 else 'Negative',
                'probability': round(probability, 2),
                'confidence': 'High' if probability > 70 or probability < 30 else 'Medium',
                'recommendation': 'Please consult a healthcare professional immediately.' if prediction[0] == 1 
                                else 'No immediate concern detected, but regular checkups are recommended.'
            }
            
            return render(request, 'result.html', {'result': result})
            
        except Exception as e:
            return render(request, 'predict.html', {'error': f"An error occurred: {str(e)}"})
    
    return render(request, 'predict.html')


def aids_hiv(request):
    return render(request, 'predict.html')


def detail(request):
    return render(request,'details.html')

