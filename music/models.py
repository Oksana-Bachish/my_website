from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Musician(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя исполнителя')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='Slug')
    context = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    age = models.IntegerField(blank=True, null=True, verbose_name='Возраст')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name='genre')
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True, verbose_name='Жанр', related_name='genre')
    tagged = models.ManyToManyField('Tagged', default=None, blank=True, related_name='tagged')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def get_absolute_url(self):
        return reverse('music:page', kwargs={'page_slug': self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Жанр')
    slug = models.SlugField(max_length=250, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music:genre', kwargs={'genre_slug': self.slug})


class Tagged(models.Model):
    tag_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, db_index=True)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('music:tag', kwargs={'tag_slug': self.slug})


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_files')

