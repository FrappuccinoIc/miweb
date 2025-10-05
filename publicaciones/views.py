from django.shortcuts import render
from .models import Publicacion
from django.core.paginator import Paginator

def foro(req):
    publicacion=Publicacion.objects.all()
    p = Paginator(publicacion, 2)

    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 🔹 Rango de páginas visibles (ejemplo: 5)
    index = page_obj.number - 1  # índice actual
    max_index = len(paginator.page_range)
    start_index = max(index - 2, 0)
    end_index = min(index + 3, max_index)
    page_range = paginator.page_range[start_index:end_index]

    return render(req, "publicaciones/foro.html", {
        "page_obj": page_obj,
        "page_range": page_range,  # 🔹 se pasa al template
    })