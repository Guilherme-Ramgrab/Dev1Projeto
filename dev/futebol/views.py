from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from futebol.models.estadio import Estadio
from futebol.forms import EstadioForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def teste(request):
    agora = datetime.now()
    saudacao = "Olá"
    if agora.hour < 12 and agora.hour > 6:
        saudacao = "Bom dia"
    mensagem = f"<html><body><h1>{saudacao} visitante!" \
               f"<br />{agora}</h1></body></html>"
    return HttpResponse(mensagem)

@login_required
def list(request):
    estadios = Estadio.objects.all().order_by('-inauguracao')
    context = {
        'estadios': estadios
    }
    return render(request, 'futebol/list_estadio.html', context)

@login_required
@permission_required('futebol.add_estadio', raise_exception=True)
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

@login_required
@permission_required('futebol.change_estadio', raise_exception=True)
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

@login_required
@permission_required('futebol.view_estadio', raise_exception=True)
def read(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    context = {
        'estadio': estadio,
    }
    return render(request, 'futebol/read_estadio.html', context)

@login_required
@permission_required('futebol.delete_estadio', raise_exception=True)
def delete(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    try:
        if request.method == 'POST':
            v_estadio_id = request.POST.get("estadio_id", None)
            if int(v_estadio_id) == estadio_id:
                estadio.delete()
                return redirect('futebol:estadio')
        else:
            context = {
                'estadio': estadio,
            }
            return render(request, 'futebol/delete_estadio.html', context)
    except:
        context = {}
        return render(request, "futebol/list_estadio.html", context)