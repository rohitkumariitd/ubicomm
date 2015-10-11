# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ubic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image_link', models.URLField()),
                ('description', models.TextField()),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default=b'SS', max_length=2, choices=[(b'SS', b'session'), (b'SR', b'series')])),
            ],
        ),
        migrations.CreateModel(
            name='UbicInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_index', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('updated_description', models.TextField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WeeklySchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week_index', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=50)),
                ('image_link', models.URLField()),
                ('description', models.TextField()),
                ('ubic_instance', models.ForeignKey(to='ubic.UbicInstance')),
            ],
        ),
        migrations.AddField(
            model_name='webinar',
            name='week',
            field=models.ForeignKey(to='ubic.WeeklySchedule'),
        ),
        migrations.AddField(
            model_name='video',
            name='week',
            field=models.ForeignKey(to='ubic.WeeklySchedule'),
        ),
        migrations.AddField(
            model_name='ubicinstance',
            name='registrations',
            field=models.ManyToManyField(to='ubic.User'),
        ),
        migrations.AddField(
            model_name='ubicinstance',
            name='ubic',
            field=models.ForeignKey(to='ubic.Ubic'),
        ),
        migrations.AddField(
            model_name='ubic',
            name='user',
            field=models.ForeignKey(to='ubic.User'),
        ),
        migrations.AddField(
            model_name='resource',
            name='week',
            field=models.ForeignKey(to='ubic.WeeklySchedule'),
        ),
    ]
