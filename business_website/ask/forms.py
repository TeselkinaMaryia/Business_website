from django import forms
from . import models


class QuestionForm(forms.Form):
    auther = forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    department = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'If you work here, write your department or post'}),
                                 required=False)
    your_question = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your question?'}))

    class Meta:
        model = models.Question
        fields = ('auther', 'department', 'your_question')


class CommentForm(forms.Form):
    your_comment = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a comment'}))

    class Meta:
        model = models.Comments
        fields = 'your_comment'
