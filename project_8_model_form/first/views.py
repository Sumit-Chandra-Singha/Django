from django.shortcuts import render
from first.forms import StudentForm

# Create your views here.
def home(request):
    std = StudentForm()
    return render(request,'home.html',{'form':std})