from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    membership_type = forms.ChoiceField(choices=User.MEMBERSHIP_CHOICES)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "membership_type", "phone")
