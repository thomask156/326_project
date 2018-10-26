from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from argue_app.models import *
from argue_app.forms import *
from argue_app.serializers import *
from django.urls import reverse

import logging
import random


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
               'user': request.user
               }
    return render(request, 'pages/chat.html', context)


def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            names = ["Alpaca", "Cat", "Cattle", "Chicken", "Dog", "Donkey", "Ferret",
                     "Gayal", "Goldfish", "Guppy", "Horse", "Koi", "Llama", "Sheep", "Yak"
            ]

            user.first_name = "Anonymous"
            user.last_name = random.choice(names)
            user.save()

            profile = Profile(bio = "", rank = 0, user = user)
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


def LobbyView(request):
    context = {'title': "Lobby",
               'user': request.user
               }
    return render(request, 'pages/lobby.html', context)


def ErrorView(request):
    context = {'title': "Error",
               }
    return render(request, 'shared/error.html', context)


def LobbyCreateView(request):
    contex = {'title': "Create Lobby",
              'topics': Topic.objects.all()
              }
    return render(request, 'pages/create_lobby.html', contex)
