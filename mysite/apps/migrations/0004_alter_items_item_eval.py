# Generated by Django 3.2.9 on 2022-03-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20220312_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_eval',
            field=models.IntegerField(default=0),
        ),
    ]