# Generated by Django 3.2.9 on 2022-03-24 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0017_alter_items_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='first',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='images',
            name='last',
            field=models.CharField(default='', max_length=20),
        ),
    ]
