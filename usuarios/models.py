from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=40, verbose_name="Nombre de Usuario")
    descripcion = models.TextField(verbose_name = "Descripción")
    imagen = models.ImageField(upload_to="projects", verbose_name="Perfil")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última vez actualizado")

    def __str__(self): return self.username