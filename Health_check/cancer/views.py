import os
import pickle
import numpy as np
from django.shortcuts import render
from django.conf import settings

# Load model and scaler
MODEL_PATH = os.path.join(settings.BASE_DIR, 'cancer', 'ml_model', 'model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, 'cancer', 'ml_model', 'scaler.pkl')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)
with open(SCALER_PATH, 'rb') as f:
    scaler = pickle.load(f)

def predict(request):
    if request.method == 'POST':
        try:
            # List of expected feature names
            feature_names = [
                'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
                'smoothness_mean', 'compactness_mean', 'concavity_mean',
                'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
                'radius_se', 'texture_se', 'perimeter_se', 'area_se',
                'smoothness_se', 'compactness_se', 'concavity_se',
                'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
                'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
                'smoothness_worst', 'compactness_worst', 'concavity_worst',
                'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
            ]
            
            # Extract and validate form data
            features = []
            for feature in feature_names:
                value = request.POST.get(feature)
                if value is None or value.strip() == '':
                    return render(request, 'cancer/predict.html', {
                        'error': f'Missing or empty value for {feature}. Please fill all fields.'
                    })
                features.append(float(value))
            
            # Convert to numpy array and scale
            features_array = np.array(features).reshape(1, -1)
            features_scaled = scaler.transform(features_array)
            
            # Predict
            prediction = model.predict(features_scaled)[0]
            probability = model.predict_proba(features_scaled)[0][1] * 100  # Probability of malignant
            
            # Prepare result
            result = 'Malignant' if prediction == 1 else 'Benign'
            confidence = f"{probability:.2f}% probability of being Malignant"
            
            return render(request, 'cancer/result.html', {
                'result': result,
                'confidence': confidence
            })
        except (ValueError, TypeError) as e:
            return render(request, 'cancer/predict.html', {
                'error': 'Please enter valid numerical values for all fields.'
            })
    return render(request, 'cancer/predict.html')



def cancer_details(request):
    return render(request, 'cancer/details.html')