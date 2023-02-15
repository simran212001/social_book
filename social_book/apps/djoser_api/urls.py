
from django.urls import re_path, include,path
from apps.djoser_api.views import *
djoserapi_urlpatterns = [
    path('generic-user/',UserGeneric.as_view()),
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
    re_path(r'^api/v1/', include('djoser.urls.jwt')),
]