from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profile(r):
    if r.method == 'POST':
        form = forms.Profile_form(r.POST)
        if form.is_valid():
            form.save()
            return redirect('add_profile')
    else:
        form = forms.Profile_form()
    return render(r, 'add_profile.html',{'form': form})
