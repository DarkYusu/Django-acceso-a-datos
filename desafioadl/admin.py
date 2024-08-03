from django.contrib import admin
from .models import Tarea, SubTarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada')
    search_fields = ('descripcion',)

@admin.register(SubTarea)
class SubTareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'eliminada', 'tarea')
    search_fields = ('descripcion',)
    list_filter = ('tarea',)
