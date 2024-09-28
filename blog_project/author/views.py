from django.shortcuts import render
from author.froms import Author_form
 
# Create your views here.
def add_author(r):
    author = Author_form()
    return render(r, 'add_author.html',{'author': author})