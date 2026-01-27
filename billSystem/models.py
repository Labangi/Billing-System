from django.db import models


# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    role=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)


