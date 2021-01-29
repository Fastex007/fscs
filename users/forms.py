from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


user = get_user_model()


class PlaceholderAuthForm(AuthenticationForm):

    class Meta:
        model = user
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(PlaceholderAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': self.fields['username'].label})
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'placeholder': self.fields['password'].label})
