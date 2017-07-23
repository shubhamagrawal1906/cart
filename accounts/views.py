# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import View
from .models import User
from rest_framework import generics, response, permissions, views, status
from .serializers import UserCreateSerializer, UserLoginSerializer, UserDetailSerializer

# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCreateSerializer

class UserLoginAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(generics.ListAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDetailSerializer
    def get_queryset(self):
        user_obj = User.objects.filter(username=self.request.user)
        return user_obj
