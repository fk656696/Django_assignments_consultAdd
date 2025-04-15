from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, blank=True)

    class Meta:
        app_label = 'Loginify'

    def __str__(self):
        return self.username