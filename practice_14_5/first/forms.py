from django import forms
from first.models import PracticeModel
from django.forms.widgets import NumberInput
import datetime


# class PracticeForm(forms.ModelForm):
#     class Meta:
#         model = PracticeModel
#         fields = '__all__'

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class PracticeForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_address = forms.EmailField(required = False)
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors4 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    # model_choice = forms.ModelChoiceField(queryset = MyModel.objects.all(),initial = 0)
    first_name = forms.CharField(initial='Your first name')
    last_name = forms.CharField(initial='Your last name')
    email_address = forms.EmailField(label="Please enter your email address")
    message = forms.CharField(max_length = 10)