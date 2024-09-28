from django import forms
from author.models import Author
 
# Create your views here.
class Author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'