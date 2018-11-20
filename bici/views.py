from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from bici.models import Bici

# Create your views here.
class ListaBici(ListView):
	model = Bici
	template_name = 'bici/listar.html'

def VerMapa(request):
    return render(request, 'bici/mapa.html', {})


def Scaner(request):
    return render(request, 'bici/qr.html', {})