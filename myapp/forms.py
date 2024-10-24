# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from .models import VastuUpload

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

# class VastuCheckForm(forms.Form):
#     room = forms.ModelChoiceField(queryset=Room.objects.all())
#     direction = forms.ModelChoiceField(queryset=Direction.objects.all())


from django import forms
from .models import VastuUpload

class VastuCheckForm(forms.ModelForm):
    class Meta:
        model = VastuUpload
        fields = ['house_plan', 'direction']
        widgets = {
            'direction': forms.RadioSelect(choices=[
                ('N', 'North'),
                ('S', 'South'),
                ('E', 'East'),
                ('W', 'West')
            ])
        }
