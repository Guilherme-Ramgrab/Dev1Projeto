from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime
from futebol.models.estadio import Estadio
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