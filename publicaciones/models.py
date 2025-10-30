from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = "Nombre")
    
    created = models.DateTimeField(auto_now = True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self): return self.nombre
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    usuario = models.CharField(max_length=20)
    descripcion = models.TextField(verbose_name = "Descripción")
    imagen = models.ImageField(upload_to="projects", verbose_name="Imagen")
    categories = models.ManyToManyField(Categoria, verbose_name = "Categorias")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): return self.titulo