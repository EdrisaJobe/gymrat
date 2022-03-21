from django.urls import path
from . import views
from .views import Workout, AddWorkout, UpdateWorkout, DeleteWorkout

# setting name of app
app_name = 'main'

urlpatterns = [
    
    # login
    path('',views.login_form, name='login'),
    
    # nav tabs
    path('calories',views.calories,name='calories'),
    path('facts', views.facts,name='facts'),
    
    # dashboard <add,update,delete>
    path('log-workout', AddWorkout.as_view(), name='log'),
    path('update-workout/<int:pk>', UpdateWorkout.as_view(), name='update'),
    path('delete-workout/<int:pk>', DeleteWorkout.as_view(), name='delete-workout'),
    
    
    # home/register
    path('home', Workout.as_view(), name='home'),
    path('register', views.register, name='register')
]
