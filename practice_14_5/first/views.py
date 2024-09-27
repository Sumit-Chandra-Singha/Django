from django.shortcuts import render, redirect
from first.forms import PracticeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST)
        if form.is_valid():
            print(form)
            subject = "Contact" 
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home.html")
      
    form = PracticeForm()

    return render(request, 'home.html', {'form': form})