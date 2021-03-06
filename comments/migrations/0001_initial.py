# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-18 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_auto_20190218_1556'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('disabled', models.BooleanField(default=False, verbose_name='禁用评论')),
                ('content', models.CharField(max_length=1000, verbose_name='评论内容')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books', verbose_name='书籍ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Passport', verbose_name='用户ID')),
            ],
            options={
                'db_table': 's_comment_table',
            },
        ),
    ]
