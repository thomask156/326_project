import os
from django.conf.urls import include, url
from rest_framework import routers
from argue_app.api import *
from argue_app.views import *
from django.urls import path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'argue_app'),
)

router = routers.DefaultRouter(trailing_slash=False)

argue_api_patterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    url(r'^create_argument/', ArgumentCreateView,name='create_argument'),
    url(r'^argument_list/', ArgumentListView, name='argument_list'),
    url(r'^profile', ProfileView, name='profile'),
    url(r'^chat/', ChatView, name='chat'),
    path('argument/<int:argument_id>/', ArgumentView, name='argument'),
    url(r'^edit_profile/', EditProfileView,name='edit_profile'),
]