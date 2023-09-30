from .models import Text
from django import forms
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model = Text
        fields = ('text',)
