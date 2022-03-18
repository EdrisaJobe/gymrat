from django.urls import path
from . import views
from django.views.generic.base import RedirectView

# setting name of app
app_name = 'main'

urlpatterns = [
    
    # login
    path('',views.login_form, name='login'),
    
    # nav tabs
    path('calories',views.calories,name='calories'),
    
    # home/register
    path('home', views.index ,name='home'),
    path('register', views.register, name='register')
]
