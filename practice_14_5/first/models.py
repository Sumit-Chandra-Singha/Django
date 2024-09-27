from django.db import models
from django import forms

# Create your models here.
class PracticeModel(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
