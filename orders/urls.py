from django.conf.urls import url, include

from .views import (
    OrderCreateAPIView,
    OrderListAPIView,
    OrderDetailAPIView,
    OrderValidateAPIView,
    )

urlpatterns = [
    url(r'^validate/(?P<token>[a-f0-9]{32})/$', OrderValidateAPIView.as_view(), name='validate'),
    url(r'^create/$', OrderCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', OrderDetailAPIView.as_view(), name='get'),
    url(r'^$', OrderListAPIView.as_view(), name='all'),
]
