# Generated by Django 3.2.9 on 2022-03-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='universities',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
