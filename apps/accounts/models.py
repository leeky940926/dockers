from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(
        max_length=500, 
        null=True
    )
    last_password_changed_at = models.DateTimeField(null=True)
    last_visit = models.DateTimeField(null=True)
