# Generated by Django 4.2.20 on 2025-05-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0023_rename_image_pizza_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='photo',
        ),
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='pizzas/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
