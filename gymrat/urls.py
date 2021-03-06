"""gymrat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # home view
    path('', include('app.urls')),
    
    # nav tab views
    path('calories', include('app.urls')),
    path('facts', include('app.urls')),
    path('recipes', include('app.urls')),
    
    # paths for dashboard buttons
    path('log-workout', include('app.urls')),
    path('update-workout', include('app.urls')),
    path('delete-workout', include('app.urls')),
    
    # register/login views
    path('home', include('app.urls')),
    path('register', include('app.urls')),
    
]
