from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=30, blank=True)
    about_me = models.TextField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    messages = models.CharField(max_length=10000,blank=True) 
    
    def __str__(self):
        return f"{self.user.username}'s Profile"