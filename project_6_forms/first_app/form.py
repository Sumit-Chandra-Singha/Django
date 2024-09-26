from typing import Any
from django import forms
from django.core import validators

# widgets == field to html input
class contact(forms.Form):
    name = forms.CharField(label="User Name",  help_text='max 50 characters',required=False,
    widget= forms.Textarea(attrs={'id':'text-area','class':'class1 class2', 'placeholder':'Enter your name'}))
    
# class validform(forms.Form):
#     name = forms.CharField(label="",widget= forms.TextInput(attrs={'placeholder':'Enter your name'}))
#     email = forms.CharField(label="",widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    
#     def clean(self):
#         cleaned_data = super().clean()
#         vname = self.cleaned_data['name']    
#         vemail = self.cleaned_data['email']
#         if len(vname) < 10:
#             raise forms.ValidationError("Name must be at least 10 characters")     
#         if '.com' not in vemail:
#             raise forms.ValidationError("email must include '.com'")
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('len must be at least 10')

class validform(forms.Form):
    # name = forms.CharField(label="",widget= forms.TextInput(attrs={'placeholder':'Enter your name'}), validators=[validators.MaxLengthValidator(10, message="Enter a value with at most 10 characters")])
    # name = forms.CharField(label="",widget= forms.TextInput(attrs={'placeholder':'Enter your name'}), validators=[validators.MinLengthValidator(10, message="Enter a value with at least 10 characters")])
    name = forms.CharField(label="",widget= forms.TextInput(attrs={'placeholder':'Enter your name'}), validators=[len_check])
    # email = forms.CharField(label="",widget= forms.EmailInput(attrs={'placeholder':'Enter your email'}),validators=[validators.EmailValidator(message='Enter a valid email')])
    # age = forms.IntegerField(validators=[validators.MinValueValidator(10, message="Enter higher value"), validators.MaxValueValidator(50, message="Enter less value")])
    # file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions='pdf', message='only pdf is allowed')])


class PasswordValidation(forms.Form):
    name = forms.CharField(label="",widget= forms.TextInput(attrs={'placeholder':'Enter your name'}))
    password = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    conf_password = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder':'Re-Enter Password'}))
    
    def clean(self):
        cleaned_data = super().clean()
        vname = self.cleaned_data['name']    
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['conf_password']
        if len(vname) < 10:
            raise forms.ValidationError("Name must be at least 10 characters.")     
        if pass1 != pass2:
            raise forms.ValidationError("Password didn't match.")