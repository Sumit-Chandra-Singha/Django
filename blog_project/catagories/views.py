from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_catagory(r):
    if r.method == 'POST':
        form = forms.Catagory_form(r.POST)
        if form.is_valid():
            form.save()
            return redirect('add_catagory')
    else:
        form = forms.Catagory_form()

    return render(r, 'add_catagory.html',{'form': form})