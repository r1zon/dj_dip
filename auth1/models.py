from django.contrib.auth.models import AbstractUser
from django.db import models


# from django.contrib.auth import get_user_model
# User = get_user_model()

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    username = models.CharField(unique=False, max_length=20)
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']
