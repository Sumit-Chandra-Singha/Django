from django import forms
from profiles.models import Profile
 
# Create your views here.
class Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'