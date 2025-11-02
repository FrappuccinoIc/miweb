from django.contrib import admin
from .models import Publicacion, Usuario
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Publicacion,ProjectAdmin)