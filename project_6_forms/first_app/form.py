from django import forms

class contact(forms.Form):
    name = forms.CharField(label="User Name")
    file = forms.FileField()
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

