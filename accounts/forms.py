from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    age = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'age')
