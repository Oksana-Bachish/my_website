# Generated by Django 4.1.7 on 2024-03-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_genre_tagged_musician_genre_musician_tagged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Slug'),
        ),
    ]
