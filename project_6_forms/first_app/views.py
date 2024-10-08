from django.shortcuts import render
from . form import contact, validform, PasswordValidation

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html',{'name': name, 'email': email, 'select': select})

    return render(request, 'about.html')


def form(request):
    return render(request, 'form.html')

def djangoform(request):
    if request.method == 'POST':
        form = contact(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, 'djangoform.html', {'form': form})
    else:
        form = contact()

    return render(request, 'djangoform.html', {'form': form})

def validdata(request):
    if request.method == 'POST':
        form = validform(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = validform()

    return render(request, 'djangoform.html', {'form': form})

def validPassword(request):
    if request.method == 'POST':
        form = PasswordValidation(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidation()

    return render(request, 'djangoform.html', {'form': form})