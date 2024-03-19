from django.http import HttpResponse
from django.shortcuts import render

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Вакансии', 'url_name': 'vacancy'},
]


def index(request):
    return render(request, 'main_page/index.html')


def about(request):
    return HttpResponse('О нас')


def contact(request):
    return HttpResponse('Контакты')


def vacancy(request):
    return HttpResponse('Вакансии')
