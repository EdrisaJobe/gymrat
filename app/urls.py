from django.urls import path
from . import views

# setting name of app
app_name = 'main'

urlpatterns = [
    path('',views.index, name='home'),
    
    # register/login
    path('login', views.login_form,name='login'),
    path('register', views.register, name='register')
]
