from django.db import models

class Publicacion(models.Model):
    titulo=models.CharField(max_length=100)
    usuario=models.CharField(max_length=20)
    descripcion=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

