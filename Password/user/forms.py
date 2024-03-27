# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Must be a valid Gmail address.')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Only Gmail addresses are allowed.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'placeholder':'John Doe',
            'maxlength': '16',
            'minlength': '6',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'email',
            'id':'email',
            'type':'email',
            'placeholder':'example@gmail.com',
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'password',
            'placeholder':'password',
            'maxlength':'22',
            'minlength':'8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'placeholder':'password',
            'maxlength':'22',
            'minlength':'8'
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
