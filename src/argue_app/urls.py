import os
from django.conf.urls import include, url
from rest_framework import routers
from argue_app.api import *
from argue_app.views import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'argue_app'),
)

router = routers.DefaultRouter(trailing_slash=False)

argue_api_patterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]