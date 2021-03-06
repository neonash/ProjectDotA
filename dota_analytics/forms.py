from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'name': 'password'}))


class PasswordResetForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=254,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
    success_url = '/password_reset/done/'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        """Meta class for login."""

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )