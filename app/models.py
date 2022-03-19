from django.db import models
from django.contrib.auth.models import User

# day of week choice
class LogWorkout(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    workout_type = models.CharField(max_length=10)
    weights = models.CharField(max_length=3)
    reps = models.CharField(max_length=3)
    
    def __str__(self):
        return self.workout_type