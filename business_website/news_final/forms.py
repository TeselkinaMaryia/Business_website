from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    second_name = forms.CharField(max_length=30,
                                  widget=forms.TextInput
                                  (attrs={'class': 'form-control', 'placeholder': 'Your second name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Number of reserved places'}))
