from django import forms
from posts.models import Post
 
# Create your views here.
class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'