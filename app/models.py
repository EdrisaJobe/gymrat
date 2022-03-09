from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LogWorkout(models.Model):
    
    # link User based on inputs, local not global
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weights = models.CharField(max_length=3)
    reps = models.CharField(max_length=3)
    
    def __str__(self):
        return self.reps
   
    

class Inputs(models.Model):
    
    log = models.ForeignKey(LogWorkout, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.log