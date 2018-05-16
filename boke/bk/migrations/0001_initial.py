# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=30)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('changetime', models.DateTimeField(auto_now=True)),
                ('read', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('sex', models.TextField(default='男')),
                ('age', models.IntegerField(default=18)),
            ],
        ),
    ]
