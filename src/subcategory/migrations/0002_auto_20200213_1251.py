# Generated by Django 3.0.3 on 2020-02-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='categoryId',
            field=models.IntegerField(),
        ),
    ]
