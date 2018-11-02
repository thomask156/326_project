from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from argue_app.models import *
from argue_app.forms import *
from argue_app.serializers import *
from django.urls import reverse
import datetime
import logging
import random

from argue_app.forms import ChatMessageForm


log = logging.getLogger('argue')

###########################################################################
#                                ARGUE VIEWS                              #
#                                                                         #
###########################################################################


def HomeView(request):
    context = {'title': "Home",
               'user': request.user
               }
    return render(request, 'pages/home.html', context)


def ChatView(request):
    context = {'title': "Chat",
               'user': request.user,
               }
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            if request.user.is_authenticated:
                chat_message.writer = Profile.objects.get(user=request.user)
            chat_message.timestamp = datetime.datetime.now()
            chat_message.chat_lobby = ChatLobby.objects.get(lobby_name='Global lobby')
            chat_message.message = form.cleaned_data.get('message')
            chat_message.save()
            return redirect('chat')
    if request.method == 'GET':
        # get all messages, return them as a list
        lobby = ChatLobby.objects.get(id=1) #get this from the model
        messages = ChatMessage.objects.filter(chat_lobby=lobby)
        context["messages"] = messages
        return render(request, 'pages/chat.html', context)
    return render(request, 'pages/chat.html', context)


def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            names = ["Alpaca", "Cat", "Cattle",
                     "Chicken", "Dog", "Donkey",
                     "Ferret", "Gayal", "Goldfish",
                     "Guppy", "Horse", "Koi", "Llama",
                     "Sheep", "Yak"
            ]

            user.first_name = "Anonymous"
            user.last_name = random.choice(names)
            user.save()

            profile = Profile(bio = "Lorem ipsum, people", rank = 0, user = user)
            profile.save()

            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})


def ProfileView(request):

    profile = Profile.objects.get(user=request.user)
    my_args = profile.lobby_set.all().values_list('argument', flat=True)

    context = {'title'    : "Profile",
               'user'     : request.user,
               'profile'  : profile,
               'arguments': my_args
               }
    return render(request, 'pages/profile.html', context)


def LobbyListView(request):

    lobby_tuples = []
    lobbies = Lobby.objects.all()
    for lobby in lobbies:
        lobby_tuples.append({"lobby" : lobby,
                         'count' : lobby.participants.count()})

    context = {'title': "Lobby List",
               'user': request.user,
               'lobbies': lobby_tuples
               }
    return render(request, 'pages/lobby_list.html', context)


def ErrorView(request):
    context = {'title': "Error",
               }
    return render(request, 'shared/error.html', context)


def LobbyCreateView(request):
    contex = {'title': "Create Lobby",
              'topics': Topic.objects.all()
              }
    if request.method == "POST":
        lobby_form = CreateLobbyForm(request.POST)
        argue_form = CreateArgumentForm(request.POST)
        if lobby_form.is_valid() and argue_form.is_valid():
            lobby = lobby_form.save(commit=False)
            argument = argue_form.save(commit=False)
            argument.last_updated = datetime.datetime.now()
            argument.save()
            lobby.argument = argument
            lobby.save()
    return render(request, 'pages/create_lobby.html', contex)
