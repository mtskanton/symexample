from users.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UsernameField


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'organisation',
            'groups'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'organisation': forms.Select(attrs={
                'class': 'form-control form-control-sm',
            }),
            'groups': forms.SelectMultiple(attrs={
                'class': 'form-control form-control-sm',
            }),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(label="логин", widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control form-control-sm', 'type': 'username', 'placeholder': 'логин'}))
    password = forms.CharField(
        label="пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control form-control-sm', 'type': 'password', 'placeholder': 'пароль'}),
    )
