from django import template
from django.db.models import Count

from music.models import Genre, Tagged

register = template.Library()


@register.inclusion_tag('music/show_genre.html')
def show_genre(genre_selected=0):
    genres = Genre.objects.annotate(total=Count('name')).filter(total__gt=0)
    return {'genres': genres, 'genre_selected': genre_selected}


@register.inclusion_tag('music/show_tags.html')
def show_tags():
    return {'tags': Tagged.objects.annotate(total=Count('tag_name')).filter(total__gt=0)}
