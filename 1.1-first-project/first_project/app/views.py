import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    current_time = datetime.datetime.now().time()
    data = {'time': f'{current_time.hour}:{current_time.minute}:{current_time.hour}'}

    return render(request, template_name, context=data)


def workdir_view(request):
    template_name = 'app/workdir.html'
    list_files = os.listdir('.')
    data = {'listfiles': list_files}

    return render(request, template_name, context=data)
