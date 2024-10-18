

import os
import joblib
import pandas as pd
import logging
from django.conf import settings
from django.shortcuts import render
from .forms import PremiumPredictionForm
import traceback


logging.basicConfig(level=logging.INFO)


model_path = os.path.join(settings.BASE_DIR, 'predictor', 'saved_models', 'premium_prediction_model.pkl')
model = joblib.load(model_path)

def predict(request):
    if request.method == 'POST':
        form = PremiumPredictionForm(request.POST)
        if form.is_valid():
            input_data = form.cleaned_data
            
            
            height_cm = float(input_data['Height'])  
            height_in_m = height_cm / 100  
            bmi = float(input_data['Weight']) / (height_in_m ** 2)  

           
            features = [
                int(input_data['Age']),
                int(input_data['Diabetes']),
                int(input_data['BloodPressureProblems']),
                int(input_data['AnyTransplants']),
                int(input_data['AnyChronicDiseases']),
                height_cm,  
                float(input_data['Weight']),
                height_in_m,  
                bmi,  
                int(input_data['KnownAllergies']),
                int(input_data['HistoryOfCancerInFamily']),
                int(input_data['NumberOfMajorSurgeries'])
            ]
            
            try:
                prediction = model.predict([features])
                prediction_value = prediction[0]
                return render(request, 'predictor/result.html', {'prediction': prediction_value})
            except Exception as e:
                logging.error(f"Error during prediction: {e}")
                logging.error(traceback.format_exc())
                return render(request, 'predictor/predict.html', {'form': form, 'error': str(e)})
    
    else:
        form = PremiumPredictionForm()

    return render(request, 'predictor/predict.html', {'form': form})
    
def home(request):
    return render(request, 'predictor/home.html')
