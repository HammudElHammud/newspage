# Generated by Django 3.0.3 on 2020-02-16 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_main_pagete'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='pageLink',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
