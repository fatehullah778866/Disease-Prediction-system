from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import joblib
import numpy as np
import os

def predict(request):
    if request.method == 'POST':
        # Load model and scaler
        model_path = os.path.join('kidney', 'ml_model', 'model.pkl')
        scaler_path = os.path.join('kidney', 'ml_model', 'scaler.pkl')
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        
        # Extract features from form
        try:
            features = [
                float(request.POST.get('age')),
                float(request.POST.get('bmi')),
                float(request.POST.get('systolic_bp')),
                float(request.POST.get('diastolic_bp')),
                float(request.POST.get('fasting_blood_sugar')),
                float(request.POST.get('hba1c')),
                float(request.POST.get('serum_creatinine')),
                float(request.POST.get('bun_levels')),
                float(request.POST.get('gfr')),
                float(request.POST.get('protein_in_urine')),
                float(request.POST.get('acr')),
                float(request.POST.get('hemoglobin_levels')),
                float(request.POST.get('cholesterol_total')),
                float(request.POST.get('cholesterol_ldl')),
                float(request.POST.get('cholesterol_hdl')),
                float(request.POST.get('cholesterol_triglycerides')),
                int(request.POST.get('family_history_kidney_disease')),
                int(request.POST.get('family_history_hypertension')),
                int(request.POST.get('family_history_diabetes')),
                int(request.POST.get('previous_acute_kidney_injury')),
                int(request.POST.get('urinary_tract_infections')),
                int(request.POST.get('edema')),
                float(request.POST.get('fatigue_levels')),
                float(request.POST.get('nausea_vomiting')),
                float(request.POST.get('muscle_cramps')),
                float(request.POST.get('itching'))
            ]
            
            # Scale features
            features_scaled = scaler.transform([features])
            
            # Predict
            prediction = model.predict(features_scaled)[0]
            probability = model.predict_proba(features_scaled)[0][1]
            
            # Prepare result
            result = 'Positive' if prediction == 1 else 'Negative'
            confidence = f"{probability * 100:.2f}%"
            
            return render(request, 'kidney/result.html', {
                'result': result,
                'confidence': confidence
            })
        except Exception as e:
            error_message = f"Error processing input: {str(e)}"
            return render(request, 'kidney/predict.html', {'error': error_message})
    
    return render(request, 'kidney/predict.html')

def detail(request):
    return render(request, 'kidney/details.html')


def kidney_back(request):
    return render(request, 'kidney/predict.html')