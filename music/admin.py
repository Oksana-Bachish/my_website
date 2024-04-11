import django.contrib.admin
from django.contrib import admin
from music.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'time_create', 'bref_info']
    list_display_links = ['id', 'title']
    ordering = ['-time_create']
    search_fields = ['title']
    list_filter = ['genre__name']
    fields = ['title', 'slug', 'context', 'genre']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10

    @admin.display(description='Краткое описание', ordering='context')
    def bref_info(self, musician: Musician):
        return f'Описание {len(musician.context)} символов'

