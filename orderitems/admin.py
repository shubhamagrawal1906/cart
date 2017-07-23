# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import OrderItem

# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    fields = ['title', 'quantity', 'price', 'order']
    list_display = ['id', 'title', 'quantity', 'price', 'order', 'created_at']
    list_filter = ['id', 'title', 'quantity', 'price', 'order', 'created_at']
    search_fields = ['order__id', 'title']
    show_full_result_count=True
admin.site.register(OrderItem, OrderItemAdmin)
