from django import forms
from django.forms import fields, widgets

from .models import BlogPost, Entry

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}