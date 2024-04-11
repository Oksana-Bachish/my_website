from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.MusicHome.as_view(), name='music_index'),
    path('genre/<slug:genre_slug>/', views.MusicGenre.as_view(), name='genre'),
    path('page/<slug:page_slug>/', views.ShowPage.as_view(), name='page'),
    path('tag/<slug:tag_slug>/', views.ShowTag.as_view(), name='tag'),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('update_page/<slug:slug>', views.UpdatePage.as_view(), name='update_page'),
    path('delete_page/<slug:slug>', views.DeletePage.as_view(), name='delete_page'),
    ]
