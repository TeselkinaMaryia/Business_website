from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_staff = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'is_staff', 'is_active', 'date_joined',
                  'password')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=50,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=50,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
