from django import forms
from django.contrib.auth.models import User
from .models import Professor

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
