# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from orders.models import Order

# Create your models here.
class OrderItem(models.Model):
    title = models.CharField(max_length=200, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)
