from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from models import *
from forms import *
from serializers import *
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
    return render(request, 'home/home.html', context)


def ErrorView(request):
    context = {'title': "Error",
               }
    return render(request, 'shared/error.html', context)