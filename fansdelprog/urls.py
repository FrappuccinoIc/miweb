from django.contrib import admin
from django.urls import path
from core import views as views_core
from publicaciones import views as views_publicacion # Importar las funciones o métodos que quieres ejecutar al acceder una ruta

# Guardar cada nueva ruta aqui
urlpatterns = [
    path('', views_core.home, name = 'home'), # ('ruta de acceso, ej: tupagina.com/foro/comentarios/:id', función o método a ejecutar al acceder, alias de ruta)
    path('faq/', views_core.faq),
    path('redes_sociales/', views_core.redes_sociales),
    path('galeria/', views_core.galeria),
    path('foro/', views_publicacion.foro),
    path('admin/', admin.site.urls),
]