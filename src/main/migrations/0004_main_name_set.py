# Generated by Django 3.0.3 on 2020-02-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200209_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='name_set',
            field=models.CharField(default='-', max_length=20),
        ),
    ]
