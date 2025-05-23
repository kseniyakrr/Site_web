# Generated by Django 3.2.16 on 2025-04-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название пиццы')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('diameter', models.PositiveIntegerField(verbose_name='Диаметр (см)')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступна для заказа')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')),
                ('image', models.ImageField(blank=True, upload_to='pizzas/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
                'ordering': ['name'],
            },
        ),
    ]
