from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Publicacion

def foro(req):
    publicacion=Publicacion.objects.all()
    p = Paginator(publicacion, 2)
    num_pag = req.GET.get('page', 1)    # Segundo arg es default

    try: pag = p.page(num_pag)
    except: pag = p.page(1)

    return render(req, "publicaciones/foro.html", {"paginacion": pag, "num_posts": len(publicacion)})