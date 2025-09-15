from django.shortcuts import render
import joblib
import numpy as np
from django.contrib.auth.decorators import login_required

def predicts(request):
    if request.method == 'POST':
        try:
            # Get form data
            pregnancies = float(request.POST.get('pregnancies'))
            glucose = float(request.POST.get('glucose'))
            blood_pressure = float(request.POST.get('blood_pressure'))
            skin_thickness = float(request.POST.get('skin_thickness'))
            insulin = float(request.POST.get('insulin'))
            bmi = float(request.POST.get('bmi'))
            diabetes_pedigree = float(request.POST.get('diabetes_pedigree'))
            age = float(request.POST.get('age'))
            
            # Load model and scaler
            with open('diabetes/ml_model/model.pkl', 'rb') as f:
                model = joblib.load(f)
            
            with open('diabetes/ml_model/scaler.pkl', 'rb') as f:
                scaler = joblib.load(f)
            
            with open('diabetes/ml_model/imputer.pkl', 'rb') as f:
                imputer = joblib.load(f)
            
            # Prepare input data
            input_data = np.array([[
                pregnancies, glucose, blood_pressure, skin_thickness,
                insulin, bmi, diabetes_pedigree, age
            ]])
            
            # Handle missing values (if any zeros in critical fields)
            input_data = imputer.transform(input_data)
            
            # Scale the data
            scaled_data = scaler.transform(input_data)
            
            # Make prediction
            prediction = model.predict(scaled_data)
            probability = model.predict_proba(scaled_data)[0][1] * 100
            
            # Prepare result
            result = {
                'prediction': 'Diabetic' if prediction[0] == 1 else 'Not Diabetic',
                'probability': round(probability, 2),
                'risk_level': 'high' if probability > 70 else 
                              'medium' if probability > 30 else 'low'
            }
            
            return render(request, 'results.html', {'result': result})
            
        except Exception as e:
            error = f"An error occurred: {str(e)}"
            return render(request, 'predicts.html', {'error': error})
    
    return render(request, 'predicts.html')

def diabetic(request):
    return render(request, 'predicts.html')


def details(request):
    return render(request, 'details.html')