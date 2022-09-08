from django.db import models
from datetime import date


class Persons (models.model):
    First_name = models.CharField(max_length=28 )
    Last_name = models.CharField(max_length=28)
    Date_of_birth = models.DateField()
    Sons = models.IntegerField()

# Create your models here.
