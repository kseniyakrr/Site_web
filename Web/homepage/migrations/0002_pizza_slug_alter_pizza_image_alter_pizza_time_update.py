# Generated by Django 4.2.20 on 2025-04-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pizzas/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время обновления'),
        ),
    ]
