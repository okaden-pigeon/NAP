# Generated by Django 3.2.9 on 2022-03-12 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20220305_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='is_deal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='icon',
            field=models.ImageField(upload_to='../images'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
    ]
