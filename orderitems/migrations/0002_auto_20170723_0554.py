# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderitems', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]
