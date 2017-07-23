from django.conf.urls import url, include
from django.contrib.auth.models import User

from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserDetailAPIView
    )

urlpatterns = [
    url(r'^signup/$', UserCreateAPIView.as_view(), name='signup'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^profile/$', UserDetailAPIView.as_view(), name='profile'),
    # url(r'^signup/$', UserCreateAPIView.as_view(), name='signup')
]
