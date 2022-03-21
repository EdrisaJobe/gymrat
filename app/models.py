from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# day of week choice
class LogWorkout(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    
    ### USER INPUTS ###
    current_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    workout_type = models.CharField(max_length=10)
    weights = models.CharField(max_length=3)
    reps = models.CharField(max_length=3)
    
    def __str__(self):
        return self.current_date