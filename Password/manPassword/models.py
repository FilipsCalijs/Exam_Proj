from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, default="-")  # Use blank=True and default="-" to make it optional
    password = models.CharField(max_length=255)
    date_of_creation = models.DateTimeField(auto_now_add=True)  # Automatically set the date of creation when an instance is created
    last_used = models.DateTimeField(auto_now=True)
    unique_id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)  # Use blank=True to make it optional
    
    def __str__(self):
        return f"{self.user.username}'s Manager"
