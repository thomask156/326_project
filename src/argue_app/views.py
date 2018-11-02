from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from argue_app.models import *
from argue_app.forms import *
from argue_app.serializers import *
import datetime
import logging
import random

from argue_app.forms import ChatMessageForm


log = logging.getLogger('argue')

###########################################################################
#                                ARGUE VIEWS                              #
#                                                                         #
###########################################################################


@login_required(login_url='/auth/login/')
def HomeView(request):
    context = {'title': "Home",
               'user': request.user
               }
    return render(request, 'pages/home.html', context)


@login_required(login_url='/auth/login/')
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


@login_required(login_url='/auth/login/')
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


@login_required(login_url='/auth/login/')
def ProfileView(request):

    profile = Profile.objects.get(user=request.user)
    my_args = profile.argument_set.all()

    context = {'title'    : "Profile",
               'user'     : request.user,
               'profile'  : profile,
               'arguments': my_args
               }
    return render(request, 'pages/profile.html', context)


@login_required(login_url='/auth/login/')
def ArgumentListView(request):
    argument_tuples = []
    arguments = reversed(Argument.objects.all())
    for argument in arguments:
        argument_tuples.append({"argument" : argument,
                         'count' : argument.participants.count()})
    context = {'title': "Argument List",
               'user': request.user,
               'arguments': argument_tuples
               }
    return render(request, 'pages/argument_list.html', context)


def ErrorView(request):
    context = {'title': "Error",
               }
    return render(request, 'shared/error.html', context)


@login_required(login_url='/auth/login/')
def ArgumentCreateView(request):
    contex = {'title': "Create Argument",
              'topics': Topic.objects.all()
              }
    if request.method == "POST":
        argue_form = CreateArgumentForm(request.POST)
        if argue_form.is_valid():
            argument = argue_form.save(commit=False)
            argument.last_updated = datetime.datetime.now()
            argument.status = Status.objects.get(status_name='Ongoing')
            chat_lobby = ChatLobby(lobby_name=argument.argument_name + " lobby")
            chat_lobby.save()
            argument.chat_lobby = chat_lobby
            argument.creator = Profile.objects.get(user=request.user)
            argument.save()
    return render(request, 'pages/create_argument.html', contex)
