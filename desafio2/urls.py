"""desafio2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from desafioadl.views import recupera_tareas_y_sub_tareas, crear_nueva_tarea, crear_sub_tarea, elimina_tarea, elimina_sub_tarea, imprimir_en_pantalla

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recupera_tareas_y_sub_tareas, name='recupera_tareas_y_sub_tareas'),
    path('crear_tarea/', crear_nueva_tarea, name='crear_nueva_tarea'),
    path('crear_sub_tarea/', crear_sub_tarea, name='crear_sub_tarea'),
    path('eliminar_tarea/<int:tarea_id>/', elimina_tarea, name='elimina_tarea'),
    path('eliminar_sub_tarea/<int:subtarea_id>/', elimina_sub_tarea, name='elimina_sub_tarea'),
    path('imprimir/', imprimir_en_pantalla, name='imprimir_en_pantalla'),
]
