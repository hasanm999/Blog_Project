from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=60)
    phone_number = forms.CharField(max_length=11)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


# forms.py
from django import forms
from django.contrib.auth import authenticate, get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def get_user(self):
        return self.user_cache

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct username and password."
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")
        return self.cleaned_data
