from django import forms
class UpdateForm(forms.Form):
    username=forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=30, required=False)
    about_me = forms.CharField(required=False)
    image = forms.ImageField(required=False)