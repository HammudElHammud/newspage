# Generated by Django 3.0.3 on 2020-02-19 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contantform', '0002_auto_20200219_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cont',
            old_name='name',
            new_name='Name',
        ),
    ]
