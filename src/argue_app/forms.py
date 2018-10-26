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

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']