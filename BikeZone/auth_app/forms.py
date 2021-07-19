from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First Name',
            }),

            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last Name'
            }),

            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
        }


