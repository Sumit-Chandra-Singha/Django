from typing import Any
from django import forms

# widgets == field to html input
class contact(forms.Form):
    name = forms.CharField(label="User Name",  help_text='max 50 characters',required=False,
    widget= forms.Textarea(attrs={'id':'text-area','class':'class1 class2', 'placeholder':'Enter your name'}))
    
class validform(forms.Form):
    name = forms.CharField(label="",widget= forms.TextInput(attrs={'placeholder':'Enter your name'}))
    email = forms.CharField(label="",widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    
    # def clean_name(self):
    #     vname = self.cleaned_data('name')     
    #     if len(vname) < 10:
    #         raise forms.ValidationError("Name must be at least 10 characters")
    #     return vname

    def clean(self):
        cleaned_data = super().clean()
        vname = self.cleaned_data['name']    
        vemail = self.cleaned_data['email']
        if len(vname) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")     
        if '.com' not in vemail:
            raise forms.ValidationError("email must include '.com'")