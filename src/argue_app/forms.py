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


class CreateLobbyForm(forms.ModelForm):
    class Meta:
        model = Lobby
        fields = ['max_participants']


class CreateArgumentForm(forms.ModelForm):
    class Meta:
        model = Argument
        fields = ['topic', 'description', 'argument_name']


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']
