from django.shortcuts import render,redirect
from users.roomidform import RoomIdForm
from django.contrib.auth.decorators import login_required
from chat.models import Rooms
from django.contrib import messages
import uuid,random
@login_required
def createroom(request):
    if request.method=='GET':
        id=uuid.uuid1()
        Rooms.objects.create(id=id)
        return redirect("room",room_name=id)
@login_required
def roomno(request):
    inp = RoomIdForm(request.POST or None)
    if request.method == 'POST' and inp.is_valid():
        id=inp.cleaned_data['roomid']
        if Rooms.objects.filter(id=id).count()>0:
            return redirect("room",room_name=id)
        else:
            messages.error(request, 'Room id does not exist')
            return render(request, "room.html", {'form':inp})
    else:
        return render(request, "room.html", {'form':inp})