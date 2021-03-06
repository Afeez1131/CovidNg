# Generated by Django 3.0.5 on 2020-05-14 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('states_affected', models.CharField(max_length=200)),
                ('lab_confirmed', models.CharField(max_length=200)),
                ('admitted', models.CharField(max_length=200)),
                ('discharged', models.CharField(max_length=200)),
                ('death', models.CharField(max_length=200)),
            ],
        ),
    ]
