from django import forms
from .models import Bin



class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'label': "Username"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
        attrs={
            'class': "form-control",
            'label': "Password"
        }
        )
    )


class UserCreationForm(forms.Form):
    class Meta:
        fields = ('username', 'email', 'name', 'password1', 'password2')


class CreateBinForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = [
            'name',
            'ip_address'
        ]
