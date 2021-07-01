from .models import *;
from django import forms;

MAX_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields =['content']
