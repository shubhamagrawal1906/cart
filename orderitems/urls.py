from django.conf.urls import url, include

from .views import (
    OrderItemCreateAPIView,
    OrderItemListAPIView,
    # UserDetailAPIView
    )

urlpatterns = [
    url(r'^create/$', OrderItemCreateAPIView.as_view(), name='create'),
    url(r'^(?P<order>[0-9]+)/$', OrderItemListAPIView.as_view(), name='all'),
    # url(r'^profile/$', UserDetailAPIView.as_view(), name='profile'),
]
