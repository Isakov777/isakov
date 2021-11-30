from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = (  
        ('m', 'male'),
        ('f', 'female'),
    )

    username = models.CharField(max_length=255, unique=True)
    profile = models.ImageField(
        upload_to = 'profiles', blank = True, null =True
    )
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=255
    )
    slug = models.SlugField(blank=True, null=True)

