from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LogWorkout(models.Model):
    
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    workout_type = models.CharField(max_length=10)
    weights = models.CharField(max_length=3)
    reps = models.CharField(max_length=3)
    time_hr = models.CharField(max_length=2)
    time_min = models.CharField(max_length=2)
    
    def __str__(self):
        return self.workout_type