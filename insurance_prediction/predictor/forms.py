from django import forms

class PremiumPredictionForm(forms.Form):
    Age = forms.IntegerField(label="Age", min_value=0)
    Diabetes = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Diabetes")
    BloodPressureProblems = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Blood Pressure Problems")
    AnyTransplants = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Any Transplants")
    AnyChronicDiseases = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Any Chronic Diseases")
    Height = forms.FloatField(label="Height (cm)", min_value=0)  # Ensure this field exists
    Weight = forms.FloatField(label="Weight (kg)", min_value=0)
    Height_in_m = forms.FloatField(label="Height (m)", min_value=0)
    BMI = forms.FloatField(label="BMI", min_value=0)
    KnownAllergies = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Known Allergies")
    HistoryOfCancerInFamily = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="History of Cancer in Family")
    NumberOfMajorSurgeries = forms.IntegerField(label="Number of Major Surgeries", min_value=0)

