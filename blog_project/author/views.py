from django.shortcuts import render, redirect
from . import forms
 
# Create your views here.
def add_author(r):
    if r.method == 'POST':
        form = forms.Author_form(r.POST)
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = forms.Author_form()

    return render(r, 'add_author.html',{'form': form})