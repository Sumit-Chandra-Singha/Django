from django.shortcuts import render
from first.forms import StudentForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            form.save()
            print(form.changed_data)
    else:
        form = StudentForm()
    return render(request,'home.html',{'form':form})