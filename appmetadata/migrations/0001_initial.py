# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppMetaData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(help_text=b'Title of  your URL', max_length=500, verbose_name='Title', blank=True)),
                ('meta_desc', models.TextField(help_text=b'Meta Description', max_length=1500, verbose_name='Meta Description', blank=True)),
                ('meta_key', models.TextField(help_text=b'Meta Keywords', max_length=1500, verbose_name='Meta Keywords', blank=True)),
            ],
            options={
                'verbose_name': 'Meta data',
                'verbose_name_plural': 'Meta data',
            },
        ),
    ]
