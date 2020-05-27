from django import forms

from .models import Bin

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CreateBinForm(forms.ModelForm):
    class Meta:
        model = Bin
        fields = [
            'name',
            'ip_address'
         ]