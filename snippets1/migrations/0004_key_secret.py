# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-10 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets1', '0003_auto_20170313_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key_Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(default=None, max_length=200, unique=True)),
                ('secret', models.TextField(default=None, max_length=200, unique=True)),
            ],
            options={
                'ordering': ('key',),
            },
        ),
    ]
