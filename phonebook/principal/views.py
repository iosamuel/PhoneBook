from django.shortcuts import render_to_response
from principal.models import Datos

def index(request):
	datos = Datos.objects.all().order_by('-id')
	return render_to_response("index.html", {"datos":datos})

def detalle(request, id):
	dato = Datos.objects.get(pk=id)
	return render_to_response("detalle.html", {"dato":dato})