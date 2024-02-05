from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная",
        "content": "Главная страница магазина STORE",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "bool": False,
    }

    return render(request, "index.html", context)


def about(request):
    return HttpResponse("О нас")
