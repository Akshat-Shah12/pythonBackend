from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    sap = models.IntegerField(default=15)
    cgpa = models.FloatField(default=15)
    branch = models.CharField(max_length=100)