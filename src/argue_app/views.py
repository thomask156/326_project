from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from argue_app.models import *
from argue_app.forms import *
from argue_app.serializers import *
import datetime
import logging
from argue_app.forms import ChatMessageForm

log = logging.getLogger('argue')


###########################################################################
#                                ARGUE VIEWS                              #
#                                                                         #
###########################################################################


@login_required(login_url='/auth/login/')
def ChatLobbyView(request, chat_lobby_id=0):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            if request.user.is_authenticated:
                chat_message.writer = Profile.objects.get(user=request.user)
            chat_message.timestamp = datetime.datetime.now()
            chat_message.chat_lobby = ChatLobby.objects.get(id=chat_lobby_id)
            chat_message.message = form.cleaned_data.get('message')
            chat_message.save()
    return redirect(request.POST['next_url'])


@login_required(login_url='/auth/login/')
def GlobalChatView(request):
    chat_lobby = ChatLobby.objects.get(lobby_name='Global lobby')
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            if request.user.is_authenticated:
                chat_message.writer = Profile.objects.get(user=request.user)
            chat_message.timestamp = datetime.datetime.now()
            chat_message.chat_lobby = chat_lobby
            chat_message.message = form.cleaned_data.get('message')
            chat_message.save()
            redirect('global_chat')
    context = {
        'title': "Chat",
        'user': request.user,
        'chat_lobby': chat_lobby,
    }
    return render(request, 'pages/global_chat.html', context)


@login_required(login_url='/auth/login/')
def ArgumentView(request, argument_id=0):
    argument = Argument.objects.get(id=argument_id)
    context = {'title': "Argument",
               'user': request.user,
               'chat_lobby': argument.chat_lobby,
               'argument': argument,
               }
    if request.method == 'POST':
        if 'forfeit' in request.POST:
            argument.forfeited.add(Profile.objects.get(user=request.user))
            argument.save()
            return redirect('argument', argument_id=argument_id)
        else:
            form = ChatMessageForm(request.POST)
            if form.is_valid():
                chat_message = form.save(commit=False)
                if request.user.is_authenticated:
                    chat_message.writer = Profile.objects.get(user=request.user)
                chat_message.timestamp = datetime.datetime.now()
                chat_message.chat_lobby = argument.chat_lobby
                chat_message.message = form.cleaned_data.get('message')
                chat_message.save()
                return redirect('argument', argument_id=argument_id)
    if request.method == 'GET':
        if Profile.objects.get(user=request.user) in argument.participants.all():
            # get all messages, return them as a list
            messages = ChatMessage.objects.filter(chat_lobby=argument.chat_lobby)
            context["messages"] = messages
            return render(request, 'pages/argument.html', context)
        elif argument.participants.count() < argument.max_participants:
            argument.participants.add(Profile.objects.get(user=request.user))
            argument.save()
            # get all messages, return them as a list
            messages = ChatMessage.objects.filter(chat_lobby=argument.chat_lobby)
            context["messages"] = messages
            return render(request, 'pages/argument.html', context)
        else:
            return redirect('argument_list')
    return render(request, 'pages/argument.html', context)


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


@login_required(login_url='/auth/login/')
def ProfileView(request):
    profile = Profile.objects.get(user=request.user)
    my_args = profile.argument_set.all().order_by('-last_updated')
    global_args = Argument.objects.all().order_by('-last_updated')[:20]

    context = {'title': "Profile",
               'user': request.user,
               'profile': profile,
               'arguments': my_args,
               'global_args': global_args
               }
    return render(request, 'pages/profile.html', context)


@login_required(login_url='/auth/login/')
def ArgumentListView(request):
    context = {'title': "Argument List",
               'user': request.user,
               }
    if request.method == "POST":
        argument_id = 0
        for key in request.POST:
            if 'join_' in key:
                argument_id = request.POST[key]
        return redirect('argument', argument_id=argument_id)
    else:
        argument_tuples = []
        arguments = reversed(Argument.objects.all())
        for argument in arguments:
            argument_tuples.append({"argument": argument,
                                    'count': argument.participants.count()})
        context['arguments'] = argument_tuples
    return render(request, 'pages/argument_list.html', context)


@login_required(login_url='/auth/login/')
def ArgumentCreateView(request):
    context = {'title': "Create Argument",
               'topics': Topic.objects.all()
               }

    if request.method == "POST":
        form = CreateArgumentForm(request.POST)
        if form.is_valid():
            argument = form.save(commit=False)
            argument.last_updated = datetime.datetime.now()
            argument.status = Status.objects.get(status_name='Ongoing')
            chat_lobby = ChatLobby(lobby_name=argument.argument_name + " lobby")
            chat_lobby.save()
            argument.chat_lobby = chat_lobby
            argument.creator = Profile.objects.get(user=request.user)
            argument.save()
            return redirect('argument', argument_id=argument.id)
    else:
        form = CreateArgumentForm()
    context['form'] = form
    return render(request, 'pages/create_argument.html', context)


@login_required(login_url='/auth/login/')
def EditProfileView(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        'title': "Edit Profile",
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'bio': profile.bio
    }

    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            profile.bio = form.cleaned_data['bio']

            request.user.save()
            profile.save()

            return redirect('profile')
    else:
        form = EditProfileForm()
    context['form'] = form
    return render(request, 'pages/edit_profile.html', context)
