from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Publicacion
from django.core.paginator import Paginator

def foro(req):
    publicacion=Publicacion.objects.all()
    p = Paginator(publicacion, 2)

    page_number = req.GET.get('page')

    page_obj = p.get_page(page_number)
    print("paso error")

    return render(req, "publicaciones/foro.html", {"page_obj": page_obj})