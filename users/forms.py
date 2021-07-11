from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email', 'password1', 'password2']
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
             raise ValidationError("Email exists")
        return self.cleaned_data