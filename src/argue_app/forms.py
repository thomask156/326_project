from django import forms
from django.contrib.auth.models import User
from argue_app.models import *

# class DataForm(forms.ModelForm):
#     """Form for data
#
#         """
#     class Meta:
#         model = Data
#         exclude = []

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')