from django.db import models
from django.contrib.auth.models import User
from catagories.models import Catagory
# from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.ManyToManyField(Catagory)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Name : {self.title}"