from django import forms

class loginFormulario(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.PasswordInput()