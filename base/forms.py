from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'required': True, 'class': 'form-control'}),
            'type': forms.Select(attrs={'id': 'type', 'required': True, 'class': 'form-select'}),
            'address': forms.TextInput(attrs={'id': 'address', 'required': True, 'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'id': 'telephone', 'required': True, 'class': 'form-control'})
        }
