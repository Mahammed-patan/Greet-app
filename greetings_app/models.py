from django.db import models

# Create your models here.

class Userinfo(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    Email = models.EmailField(max_length=50, unique=True)  # Ensure unique emails
    Password = models.CharField(max_length=255)  # Increased length for hashed password
