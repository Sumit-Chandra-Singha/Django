from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    fathers_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    
