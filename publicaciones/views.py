from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Publicacion
from django.core.paginator import Paginator

def foro(req):
    publicaciones = Publicacion.objects.all().order_by('id')  # puedes cambiar el orden si quieres
    paginator = Paginator(publicaciones, 1)  # ← un artículo por página

    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(req, "publicaciones/foro.html", {"page_obj": page_obj})