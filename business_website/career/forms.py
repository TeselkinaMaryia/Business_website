from django import forms
from . import models


class ApplyForm(forms.Form):
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    working_position = forms.ModelChoiceField(queryset=models.Vacancies.objects.all(), required=True)
    short_summary = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'You should write a short summary'}))
    work_in_the_office = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    online_work = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    individual_feature = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "What's your individual features?"}))

    class Meta:
        model = models.Apply
        fields = ('first_name', 'last_name', 'email', 'working_position', 'short_summary', 'work_in_the_office',
                  'online_work', 'individual_feature')
