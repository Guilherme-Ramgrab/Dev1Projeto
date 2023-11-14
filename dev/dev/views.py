from django.shortcuts import render


def index(request):
    context = {'nome': 'Ricardo'}
    return render(request, 'index.html', context)


def nome(request, nome):
    context = {'nome': nome}
    return render(request, 'index.html', context)
