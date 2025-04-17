from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, blank=True)

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    message = models.TextField(max_length=200)

class Meta:
    app_label = 'Loginify'

    def __str__(self):
        return self.username

class test(models.Model):
    test=models.Charfield(max_length=100)