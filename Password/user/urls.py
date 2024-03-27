from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Assuming 'home' is defined in views.py
    path('signup/', views.signup, name='signup'), 
    path("accounts/", include("django.contrib.auth.urls")),
]