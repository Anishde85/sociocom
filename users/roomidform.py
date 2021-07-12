from django import forms
class RoomIdForm(forms.Form):
    roomid=forms.CharField(max_length=30,required=True)