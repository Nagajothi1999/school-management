from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .constant import ROLE_CHOICES

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    country = forms.CharField(max_length=50)
    nationality = forms.CharField(max_length=50)
    mobile = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role", "country", "nationality", "mobile"]
        def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['username'].label = 'Name'