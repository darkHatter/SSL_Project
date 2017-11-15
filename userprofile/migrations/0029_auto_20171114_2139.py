# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-14 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0028_auto_20171112_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Student_category',
            field=models.IntegerField(choices=[(0, 'M.Tech. Students Ongoing'), (1, 'M.Tech. Students Completed'), (2, 'Ph.D. Students Continuing'), (3, 'Ph.D. Students Completed')], default=None),
        ),
    ]
