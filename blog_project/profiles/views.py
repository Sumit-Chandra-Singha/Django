from django.shortcuts import render

# Create your views here.
def add_profile(r):
    return render(r, 'base.html')