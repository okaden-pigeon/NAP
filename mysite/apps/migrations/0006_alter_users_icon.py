# Generated by Django 3.2.9 on 2022-03-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]
