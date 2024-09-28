from django.shortcuts import render

# Create your views here.
def add_author(r):
    return render(r, 'add_author.html')