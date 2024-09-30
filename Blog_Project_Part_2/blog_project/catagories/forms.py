from django import forms
from catagories.models import Catagory
 
# Create your views here.
class Catagory_form(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'