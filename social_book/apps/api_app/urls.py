from django.urls import path
from .import views

from django.urls import include, re_path

from apps.api_app.views import UserCreateAPIView, UserLoginAPIView

# from .views import FileView

restapi_urlpatterns = [
    re_path(r'^users/register/$', UserCreateAPIView.as_view(), name='user-register'),
    re_path(r'^users/login/$', UserLoginAPIView.as_view(), name="user-login"),
]