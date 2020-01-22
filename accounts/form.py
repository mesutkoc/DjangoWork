from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label='Username')
    password = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('Wrong User')
        return super(LoginForm,self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label='Username')
    mail = forms.CharField(max_length=100,label='Mail')
    password1 = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100,label='Password Repeat',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'mail',
            'password1',
            'password2'
        ]
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords are not same!!")
        return password2

class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
        )


