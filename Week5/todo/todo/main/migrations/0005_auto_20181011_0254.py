# Generated by Django 2.1 on 2018-10-11 02:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181004_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 11, 2, 54, 25, 15696)),
        ),
    ]
