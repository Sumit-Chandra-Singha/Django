from django.shortcuts import render

# Create your views here.
def add_profile(r):
    return render(r, 'add_profile.html')