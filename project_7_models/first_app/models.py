from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    fathes_name = models.TextField(default='Sumit')

    def __str__(self):
        return f"Roll : {self.roll} - Name : {self.name}"
    
# py manage.py makemigrations
# py manage.py migrate
