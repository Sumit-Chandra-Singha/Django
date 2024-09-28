from django.shortcuts import render

# Create your views here.
def add_post(r):
    return render(r, 'add_post.html')