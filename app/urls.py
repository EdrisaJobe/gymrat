from django.urls import path
from . import views
from .views import Workout, LogWorkout

# setting name of app
app_name = 'main'

urlpatterns = [
    
    # login
    path('',views.login_form, name='login'),
    
    # nav tabs
    path('calories',views.calories,name='calories'),
    
    # dashboard <add,update,delete>
    path('logworkout', LogWorkout.as_view(), name='logworkout'),
    path('updateworkout', Updat)
    
    
    # home/register
    path('home', Workout.as_view(), name='home'),
    path('register', views.register, name='register')
]
