from django.contrib import admin
from .models import Publicacion, Usuario, Categoria
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('usuario', 'created','updated')

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Publicacion,ProjectAdmin)