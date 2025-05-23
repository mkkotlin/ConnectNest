from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
     is_social_user = models.BooleanField(default=False)

     def __str__(self):
          return self.username
     
class Profile(models.Model):
     user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)
     bio = models.TextField(blank=True)
     profile_pic = models.ImageField(upload_to='profiles/', blank=True)

     def __str__(self):
          return self.user.username
     


