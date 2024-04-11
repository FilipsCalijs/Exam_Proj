from django.urls import path, include
from . import views

urlpatterns = [
    path("showpass/", views.showpass, name="showpass"),
    path("jsonPasswords/", views.jsonPasswords, name="jsonPasswords"),
    path('createPass/', views.createPass, name='createPass'),
    path('', include('user.urls')), 
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit_data/<data_id>', views.edit_data, name='edit_data'),
    path('filter/', views.filter, name='filter'),

]
