# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, sender, receiver):
    return render(request, 'chat/room.html', {
        'sender': sender,
        'receiver':receiver
    })