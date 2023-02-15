"""social_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings #add this
from django.conf.urls.static import static #add this

from apps.users.urls import users_urlpatterns
from apps.api_app.urls import restapi_urlpatterns
from apps.djoser_api.urls import djoserapi_urlpatterns
from apps.djoser_api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('apps.djoser_api.urls')),
    # path('',include('apps.users.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),
]
if settings.DEBUG:
    users_urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += users_urlpatterns

# urlpatterns += restapi_urlpatterns
urlpatterns += djoserapi_urlpatterns