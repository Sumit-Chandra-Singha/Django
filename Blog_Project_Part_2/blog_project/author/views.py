from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully.')
            return redirect('register')
    else:
        form = forms.RegistrationForm()

    return render(request, 'register.html',{'form': form, 'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged In Successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Login Information Incorrect.')
            return redirect('user_login')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'register.html', {'form': form, 'type': 'LOGIN'})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('user_login')

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name, password=user_pass)
#             if user is not None :
#                 messages.success(request, 'Logged In Successfully.')
#                 login(request,user)
#                 return redirect('user_login')
#             else:
#                 messages.warning(request, 'Login Information Incorrect.')
#                 return redirect('register')
    
#     else:
#         form = AuthenticationForm()
#         return render(request, 'register.html', {'form': form, 'type': 'LOGIN'})
#     # return render(request, 'register.html', {'form': form, 'type': 'LOGIN'})
