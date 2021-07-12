from django import forms
class UpdateForm(forms.Form):
    confirm_email = forms.EmailField(required=True)
    location = forms.CharField(max_length=30, required=False)
    about_me = forms.CharField(required=False)
    image = forms.ImageField(required=False)