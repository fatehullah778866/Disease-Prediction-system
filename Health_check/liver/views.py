from django.shortcuts import render
import joblib
import numpy as np

def home_liver(request):
    return render(request, 'liver/predict.html')

def predict_liver(request):
    if request.method == 'POST':
        # Get form data
        age = float(request.POST.get('age'))
        gender = float(request.POST.get('gender'))
        total_bilirubin = float(request.POST.get('total_bilirubin'))
        direct_bilirubin = float(request.POST.get('direct_bilirubin'))
        alkaline_phosphotase = float(request.POST.get('alkaline_phosphotase'))
        alamine_aminotransferase = float(request.POST.get('alamine_aminotransferase'))
        aspartate_aminotransferase = float(request.POST.get('aspartate_aminotransferase'))
        total_protiens = float(request.POST.get('total_protiens'))
        albumin = float(request.POST.get('albumin'))
        albumin_and_globulin_ratio = float(request.POST.get('albumin_and_globulin_ratio'))
        
        # Create feature array
        features = np.array([[
            age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
            alamine_aminotransferase, aspartate_aminotransferase, total_protiens,
            albumin, albumin_and_globulin_ratio
        ]])
        
        # Load model and scaler
        try:
            model = joblib.load('liver/ml_model/model.pkl')
            scaler = joblib.load('liver/ml_model/scaler.pkl')
            
            # Scale features
            scaled_features = scaler.transform(features)
            
            # Make prediction
            prediction = model.predict(scaled_features)[0]
            probability = model.predict_proba(scaled_features)[0][1]
            
            # Interpret prediction
            result = "Positive" if prediction == 1 else "Negative"
            confidence = round(probability * 100, 2) if prediction == 1 else round((1 - probability) * 100, 2)
            
            # Prepare context
            context = {
                'result': result,
                'confidence': confidence,
                'probability': round(probability * 100, 2),
                'input_data': {
                    'Age': age,
                    'Gender': "Male" if gender == 1 else "Female",
                    'Total Bilirubin': total_bilirubin,
                    'Direct Bilirubin': direct_bilirubin,
                    'Alkaline Phosphotase': alkaline_phosphotase,
                    'Alamine Aminotransferase': alamine_aminotransferase,
                    'Aspartate Aminotransferase': aspartate_aminotransferase,
                    'Total Protiens': total_protiens,
                    'Albumin': albumin,
                    'Albumin and Globulin Ratio': albumin_and_globulin_ratio
                }
            }
            
            return render(request, 'liver/result.html', context)
            
        except Exception as e:
            error_message = f"Error in prediction: {str(e)}"
            return render(request, 'liver/predict.html', {'error': error_message})
    
    return render(request, 'liver/predict.html')



def detail(request):
    return render(request,'liver/details.html')