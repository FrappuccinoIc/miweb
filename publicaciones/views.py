from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Publicacion

def foro(request):
    publicacion=Publicacion.objects.all().order_by('created')
    p = Paginator(publicacion, 2)
    num_pag = request.GET.get('page', 1)    # Segundo arg es default

    try: pag = p.page(num_pag)
    except: 
        pag = p.page(1)
        print("paso error")

    return render(request, "publicaciones/foro.html", {"paginacion": pag, "num_posts": len(publicacion)})