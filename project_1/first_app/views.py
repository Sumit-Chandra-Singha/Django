from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(response):
    return HttpResponse("This is first_app/home page. ")
def courses(response):
    return HttpResponse("This is first_app/courses page.")
def about(response):
    return HttpResponse("This is first_app/about page.")