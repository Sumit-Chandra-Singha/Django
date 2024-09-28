from django.db import models
from catagories.models import Catagory
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.ManyToManyField(Catagory)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Name : {self.title}, Author : {self.author}"