# Generated by Django 3.2.9 on 2022-03-23 06:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0013_alter_items_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='./images/')),
            ],
        ),
        migrations.AlterField(
            model_name='items',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 6, 20, 21, 215616, tzinfo=utc)),
        ),
    ]
