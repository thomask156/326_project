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

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    bio = forms.CharField(max_length=100)


class CreateArgumentForm(forms.ModelForm):
    class Meta:
        model = Argument
        fields = ['topic', 'description', 'argument_name', 'max_participants']


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']
