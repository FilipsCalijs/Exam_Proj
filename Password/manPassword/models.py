from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, default="-") 
    password = models.CharField(max_length=255)
    date_of_creation = models.DateTimeField(auto_now_add=True)  
    last_used = models.DateTimeField(auto_now=True)
    unique_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)  
    
    def __str__(self):
        return f"{self.user.username}'s Manager"
