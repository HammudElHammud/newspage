# Generated by Django 3.0.3 on 2020-02-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_txt', models.CharField(max_length=40)),
                ('date', models.CharField(max_length=15)),
                ('newBody', models.CharField(max_length=200)),
                ('pic', models.CharField(max_length=15)),
                ('writer', models.CharField(max_length=20)),
                ('name_set', models.CharField(default='-', max_length=20)),
            ],
        ),
    ]
