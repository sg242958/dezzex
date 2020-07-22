from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registration(models.Model):
    full_name = models.CharField(max_length=100, default="")
    dob = models.DateField()
    phone = models.CharField(max_length=12, default="")
    email = models.EmailField(max_length=100, default="")
    passport_no = models.CharField(max_length=20, default="")
    image = models.ImageField(upload_to="profile", default="")
    password = models.CharField(max_length=20, default="")
    repassword = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.phone

