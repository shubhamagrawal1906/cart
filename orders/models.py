# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import User
import uuid

# Create your models here.
class Order(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
        ('SC', 'Smart Card'),
        ('EM', 'E-Money'),
        ('EFT', 'Electronic Fund Transfer'),
        ('COD', 'Cash On Delivery')
    )
    STATUS_CHOICES = (
        ('NA', 'Not Approved'),
        ('A', 'Approved'),
        ('P', 'Packed'),
        ('S', 'Shipped'),
        ('D', 'Delivered')
    )
    total_order = models.PositiveIntegerField(default=0)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default=PAYMENT_METHOD_CHOICES[0][0])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=32, default='')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)
