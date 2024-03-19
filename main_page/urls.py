from django.urls import path
from . import views

#app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.about, name='contact'),
    path('vacancy/', views.about, name='vacancy'),
  ]
