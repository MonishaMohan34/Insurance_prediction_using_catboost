from django.db import models

class UserData(models.Model):
    age = models.IntegerField()
    diabetes = models.IntegerField(choices=[(0, "No"), (1, "Yes")], default=0)  # No = 0, Yes = 1
    blood_pressure_problems = models.IntegerField(choices=[(0, "No"), (1, "Yes")], default=0)
    any_transplants = models.IntegerField(choices=[(0, "No"), (1, "Yes")], default=0)
    any_chronic_diseases = models.IntegerField(choices=[(0, "No"), (1, "Yes")], default=0)
    height = models.FloatField()
    weight = models.FloatField()
    height_in_m = models.FloatField()
      
    bmi = models.FloatField()
    known_allergies = models.IntegerField(choices=[(0, "No"), (1, "Yes")], default=0)
    history_of_cancer_in_family = models.IntegerField(choices=[(0, "No"), (1, "Yes")], default=0)
    number_of_major_surgeries = models.IntegerField()

    def __str__(self):
        return f"UserData(age={self.age}, diabetes={self.diabetes}, blood_pressure_problems={self.blood_pressure_problems}, weight={self.weight})"
