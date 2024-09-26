from django import forms

# widgets == field to html input
class contact(forms.Form):
    name = forms.CharField(label="User Name",  help_text='max 50 characters',required=False,
    widget= forms.Textarea(attrs={'id':'text-area','class':'class1 class2', 'placeholder':'Enter your name'}))
    age = forms.CharField(widget=forms.NumberInput)
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('XS','EXTRA SMALL'),('S','SMALL'),('M','MEDIUM'),('L','LARGE'),('XL','EXTRA LARGE'),('XXL','EXTRA EXTRA LARGE')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P','PEPPERONI'),('M','MASHROOM'),('MY','MEYONEESE'),('C','CHEESE')]
    meal = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.DecimalField()
    # balance = forms.FloatField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()
    # CHOICES = [('XS','EXTRA SMALL'),('S','SMALL'),('M','MEDIUM'),('L','LARGE'),('XL','EXTRA LARGE'),('XXL','EXTRA EXTRA LARGE')]
    # size = forms.ChoiceField(choices= CHOICES)
    # MEAL = [('P','PEPPERONI'),('M','MASHROOM'),('MY','MEYONEESE'),('C','CHEESE')]
    # meal = forms.MultipleChoiceField(choices= MEAL)

