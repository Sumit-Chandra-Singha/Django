from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_post(r):
    if r.method == 'POST':
        form = forms.Post_form(r.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else:
        form = forms.Post_form()

    return render(r, 'add_post.html', {'form': form})

def edit_post(r, id):
    post = models.Post.objects.get(pk=id)
    form = forms.Post_form(instance=post)
    # print(post) 
    if r.method == 'POST':
        form = forms.Post_form(r.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(r, 'add_post.html', {'form': form})

def delete_post(r, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
