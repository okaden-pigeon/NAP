# Generated by Django 3.2.9 on 2022-03-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_alter_users_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='./images/'),
        ),
    ]