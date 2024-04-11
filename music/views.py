from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from music.forms import AddPageForm
from music.models import Musician, Tagged


class MusicHome(ListView):
    model = Musician
    template_name = 'music/music_index.html'
    context_object_name = 'pages'
    paginate_by = 3
    extra_context = {
        'title': 'Музыкальные исполнители',
        'genre_selected': 0,
    }

    def get_queryset(self):
        return Musician.objects.all()


class MusicGenre(ListView):
    template_name = 'music/music_index.html'
    context_object_name = 'pages'
    allow_empty = False

    def get_queryset(self):
        return Musician.objects.filter(genre__slug=self.kwargs['genre_slug']).select_related('genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = context['pages'][0].genre
        context['title'] = 'Категория - ' + genre.name
        context['genre_selected'] = genre.pk
        return context


# def music_index(request):
#     singers = Musician.objects.all()
#     data = {
#             'title': 'Главная страница',
#             'singers': singers,
#             'cat_selected': 0,
#         }
#     return render(request, 'music/music_index.html', context=data)

class ShowTag(ListView):
    template_name = 'music/music_index.html'
    context_object_name = 'pages'
    allow_empty = True

    def get_queryset(self):
        return Musician.objects.filter(tagged__slug=self.kwargs['tag_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tagged.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag_name
        context['genre_selected'] = None
        return context


class ShowPage(DetailView):
    model = Musician
    template_name = 'music/music_page.html'
    context_object_name = 'page'
    slug_url_kwarg = 'page_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['page'].title
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Musician, slug=self.kwargs[self.slug_url_kwarg])

# def show_page(request, page_slug):
#     page = get_object_or_404(Musician, slug=page_slug)
#     #page = Musician.objects.get(slug=page_slug)
#     data = {
#         'title': page.title,
#         'page': page,
#         'genre_selected': 1,
#     }
#     return render(request, 'music/music_page.html', data)


class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddPageForm
    template_name = 'music/music_add_page.html'
    success_url = reverse_lazy('music:music_index')
    extra_context = {'title': 'Добавление статьи'}

    def form_valid(self, form):
        m = form.save(commit=False)
        m.author = self.request.user
        return super().form_valid(form)


class UpdatePage(UpdateView):
    model = Musician
    template_name = 'music/music_add_page.html'
    extra_context = {'title': 'Редактирование статьи'}
    fields = ['title', 'photo', 'slug', 'context',  'genre', 'age']
    success_url = reverse_lazy('music:music_index')


class DeletePage(DeleteView):
    model = Musician
    success_url = reverse_lazy('music:music_index')
    template_name = 'music/music_delete_page.html'

