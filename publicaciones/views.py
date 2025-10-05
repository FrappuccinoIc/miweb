from django.shortcuts import render
from .models import Publicacion

def foro(req):
    publicacion=Publicacion.objects.all()
    return render(req, "publicaciones/foro.html", {"publicacion": publicacion})