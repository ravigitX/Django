from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'email', 'property']
