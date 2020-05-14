# Generated by Django 3.0.5 on 2020-05-14 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('total', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sample', models.CharField(max_length=200, null=True)),
                ('confirmed', models.CharField(max_length=200, null=True)),
                ('active', models.CharField(max_length=200, null=True)),
                ('discharged', models.CharField(max_length=200, null=True)),
                ('death', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
