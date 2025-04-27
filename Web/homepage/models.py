from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class AvailablePizzaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=Pizza.Status.AVAILABLE)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)  # Определяем base_slug перед использованием
            unique_slug = base_slug
            num = 1
            while Category.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    class Status(models.IntegerChoices):
        NOTAVAILABLE = 0, 'Нет в наличии'
        AVAILABLE = 1, 'Есть в наличии'
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    diameter = models.PositiveIntegerField(verbose_name='Диаметр (см)')
    is_available = models.BooleanField(choices=Status.choices, default=Status.NOTAVAILABLE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    image = models.ImageField(upload_to='pizzas/', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
    
    objects = models.Manager()
    published = AvailablePizzaManager()

    def get_absolute_url(self):
        return reverse('pizza_detail', kwargs={'pizza_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']

    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)  # Определяем base_slug перед использованием
            unique_slug = base_slug
            num = 1
            while Pizza.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)



       

