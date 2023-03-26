from django import forms
from . import models


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Subject"}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your massage'}))

    class Meta:
        model = models.Cantact
        fields = ('name', 'email', 'email', 'subject', 'message')
