# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-16 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190216_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adderss',
            name='passport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Passport', verbose_name='账户'),
        ),
    ]
