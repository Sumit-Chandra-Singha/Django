from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('this is main home')

def index(request):
    return render(request, 'index.html')