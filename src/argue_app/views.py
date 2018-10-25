from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from argue_app.models import *
from argue_app.forms import *
from argue_app.serializers import *
from django.urls import reverse

import logging
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
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form})


def ProfileView(request):
    context = {'title': "Profile",
               'user': request.user
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
              }
    return render(request, 'pages/create_lobby.html', contex)
