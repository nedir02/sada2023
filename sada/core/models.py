from django.db import models
# Create your models here.
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Ady')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Goýlan senesi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Täzelenen senesi')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Suraty', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Goýlan wagty?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Kategoriýa')
    slug = models.SlugField(max_length=95, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Önüm'
        verbose_name_plural = 'Önümler'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Kategoriyanyn ady')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriýalar'
        ordering = ['title']
