from django.contrib import admin
from .models import Entrada

class EntradaAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'updated_at') #para mostrar campos 
    search_fields = ('title', 'content', 'user__username') #para crear fitro de busqueda
    list_display = ('title', 'user', 'public', 'created_at') #para mstrar columnas
    list_filter = ('public', 'user__username') #para filtrar
    
    #este codigo es para guardar el usuario por defecto
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

# Register your models here.

admin.site.register(Entrada, EntradaAdmin)
