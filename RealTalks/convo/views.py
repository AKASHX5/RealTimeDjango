from django.shortcuts import render
# Create your views here.

def index(request, *args, **kwargs):
    context = {}
    return render(request,'index.html', {})

def room(request, room_name):
    context = {}
    return render(request,'chatroom.html', {
        "room_name":room_name
    })

