from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'number': 1, 'str': "I'm Sumit", 'name': 'sumit chandra singha',
         'title':'sumit',
         'val': [
         {'name': 'zed', 'age': 19},
         {'name': 'amy', 'age': 22},
         {'name': 'joe', 'age': 31},
         ],
         'date': datetime.datetime.now(),
         'lst': ['this','is','join','filter'],
         'lines': 'this\nis\nline\nnumber',
         'upper': 'UPPER'
        
        }
    return render(request, 'home.html', d)