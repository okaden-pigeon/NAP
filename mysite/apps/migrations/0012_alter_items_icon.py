# Generated by Django 3.2.9 on 2022-03-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_alter_users_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='icon',
            field=models.ImageField(default='./images/default_user.png', upload_to='./static/apps/'),
        ),
    ]