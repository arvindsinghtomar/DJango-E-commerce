# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0026_pro_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro_display',
            name='photo',
            field=models.ImageField(blank=True, upload_to='productimage'),
        ),
    ]