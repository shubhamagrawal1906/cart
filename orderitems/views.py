# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from .models import OrderItem, Order
from rest_framework import generics, response, permissions, views, status
from .serializers import OrderItemCreateSerializer, OrderItemListSerializer
from .pagination import Pagination
from django.core.exceptions import ValidationError

# Create your views here.
class OrderItemCreateAPIView(generics.CreateAPIView):
    model = OrderItem
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderItemCreateSerializer

class OrderItemListAPIView(generics.ListAPIView):
    model = Order
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderItemListSerializer
    pagination_class = Pagination
    order_obj = 0
    def get_queryset(self):
        if Order.objects.filter(pk=self.kwargs['order']):
            order_obj = Order.objects.filter(pk=self.kwargs['order']).first()
            if not order_obj.user == self.request.user:
                order_obj = 0
        orderitem_list = OrderItem.objects.filter(order=order_obj).order_by('created_at')
        return orderitem_list
