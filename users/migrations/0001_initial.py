# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('title', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.IntegerField()),
                ('password', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('md5', models.CharField(max_length=255)),
                ('sha1', models.CharField(max_length=255)),
                ('sha256', models.CharField(max_length=255)),
                ('registered', models.DateTimeField()),
                ('dob', models.DateTimeField()),
                ('phone', models.CharField(max_length=255)),
                ('cell', models.CharField(max_length=255)),
                ('pps', models.CharField(max_length=255)),
                ('large_picture', models.URLField()),
                ('medium_picture', models.URLField()),
                ('thumbnail_picture', models.URLField()),
            ],
        ),
    ]
