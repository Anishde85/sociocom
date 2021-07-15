from django import forms
class RoomIdForm(forms.Form):
    roomid=forms.CharField(max_length=50,required=True)