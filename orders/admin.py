# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    fields = ['total_order', 'payment_method', 'status', 'user', 'token']
    list_display = ['id', 'total_order', 'payment_method', 'status', 'user', 'token', 'created_at']
    list_filter = ['id', 'total_order', 'payment_method', 'status', 'user', 'created_at']
    search_fields = ['user__username']
    show_full_result_count=True
admin.site.register(Order, OrderAdmin)
