# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    fname = forms.CharField(max_length=30, required=True, help_text='Required.')
    lname = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'fname', 'lname', 'email',  'password1', 'password2' )

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username", required=True)
    password = forms.CharField(label="password", widget=forms.PasswordInput, required=True)


