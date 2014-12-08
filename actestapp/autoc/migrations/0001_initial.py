# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NonAdminAddAnotherModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('widgets', models.ManyToManyField(blank=True, to='autoc.NonAdminAddAnotherModel', related_name='widgets_rel_+')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
