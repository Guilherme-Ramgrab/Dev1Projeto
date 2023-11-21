from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from futebol.models.estadio import Estadio
from futebol.forms import EstadioForm
# Create your views here.


def teste(request):
    agora = datetime.now()
    saudacao = "Olá"
    if agora.hour < 12 and agora.hour > 6:
        saudacao = "Bom dia"
    mensagem = f"<html><body><h1>{saudacao} visitante!" \
               f"<br />{agora}</h1></body></html>"
    return HttpResponse(mensagem)

def list(request):
    estadios = Estadio.objects.all().order_by('-inauguracao')
    context = {
        'estadios': estadios
    }
    return render(request, 'futebol/list_estadio.html', context)

def create(request):
    if request.method == 'POST':
        form = EstadioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('futebol:estadio')
    else:
        form = EstadioForm()

    context = {
        'form': form
    }
    return render(request, 'futebol/create_estadio.html', context)

def update(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    if request.method == 'POST':
        form = EstadioForm(request.POST, instance=estadio)
        if form.is_valid():
            form.save()
            return redirect('futebol:estadio')
    else:
        form = EstadioForm(instance=estadio)

    context = {
        'form': form,
        'estadio': estadio,
    }
    return render(request, 'futebol/edit_estadio.html', context)

def read(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    context = {
        'estadio': estadio,
    }
    return render(request, 'futebol/read_estadio.html', context)