from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('signup/', views.signup, name='signup'), 
    path('logout/', views.logout, name='logout'),
    path('json/', views.json, name='json'),
    path("accounts/", include("django.contrib.auth.urls")),  
     

]