from django import forms 
from first.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll']
        # exclude = ['roll']
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            # 'roll': forms.PasswordInput()
        }
        help_texts = {
            'name': 'write full name'
        }
        error_messages = {
            'name': {'required':'Name is required'}
        }