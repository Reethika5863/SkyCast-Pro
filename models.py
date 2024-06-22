from django.db import models

# Create your models here.
class contact(models.Model):
    Mobile=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)