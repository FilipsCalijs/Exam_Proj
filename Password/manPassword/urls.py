from django.urls import path, include
from . import views

urlpatterns = [
    path("showpass/", views.showpass, name="showpass"),
    path("jsonPasswords/", views.jsonPasswords, name="jsonPasswords"),
    path('createPass/', views.createPass, name='createPass'),
    path('', include('user.urls')), 

]
