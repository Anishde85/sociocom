from django.shortcuts import render,redirect
from users.roomidform import RoomIdForm
from django.contrib.auth.decorators import login_required
@login_required
def roomno(request):
    inp = RoomIdForm(request.POST or None)
    if request.method == 'POST' and inp.is_valid():
        id=inp.cleaned_data['roomid']
        return redirect("room",room_name=id)
        
    else:
        return render(request, "room.html", {'form':inp})