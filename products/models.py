from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    preview = models.ImageField(upload_to='category/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    preview = models.ImageField(upload_to='subcategory/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    preview_small = models.ImageField(upload_to='products/small/',
                                      null=True,
                                      blank=True,
                                      verbose_name='Изображение маленькое')
    preview_middle = models.ImageField(upload_to='products/middle/',
                                       null=True,
                                       blank=True,
                                       verbose_name='Изображение среднее')
    preview_big = models.ImageField(upload_to='products/big/',
                                    null=True,
                                    blank=True,
                                    verbose_name='Изображение большое')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    subcategory = models.ForeignKey('Subcategory',
                                    on_delete=models.CASCADE,
                                    related_name='subcategory',
                                    verbose_name='Подкатегория')

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
