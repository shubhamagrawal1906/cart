# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from .models import Order, User
from rest_framework import generics, response, permissions, views, status
from .serializers import OrderCreateSerializer, OrderListSerializer, OrderDetailSerializer, OrderValidateSerializer
from .pagination import Pagination
from orderitems.views import OrderItemListAPIView
# Create your views here.
class OrderCreateAPIView(generics.CreateAPIView):
    model = Order
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderCreateSerializer

class OrderListAPIView(generics.ListAPIView):
    model = Order
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderListSerializer
    pagination_class = Pagination
    def get_queryset(self):
        user_obj = User.objects.get(username=self.request.user)
        order_list = Order.objects.filter(user=self.request.user).order_by('-created_at')
        return order_list

class OrderDetailAPIView(generics.RetrieveAPIView):
    model = Order
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = Order.objects.filter(pk=self.kwargs['pk']).filter(user=self.request.user)
        order = queryset.first()
        response = OrderItemListAPIView.as_view()
        print(response)
        return queryset

class OrderValidateAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderValidateSerializer

    def get(self, request, *args, **kwargs):
        request.data.update({'token': self.kwargs['token']})
        data = request.data
        serializer = OrderValidateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
