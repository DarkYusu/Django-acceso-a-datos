from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea, SubTarea
from .forms import TareaForm, SubTareaForm

def recupera_tareas_y_sub_tareas(request):
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return render(request, 'recupera_tareas_y_sub_tareas.html', {'tareas': tareas, 'subtareas': subtareas})

def crear_nueva_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recupera_tareas_y_sub_tareas')  # Redirige a la vista que muestra tareas y subtareas
    else:
        form = TareaForm()
    return render(request, 'crear_nueva_tarea.html', {'form': form})


def crear_sub_tarea(request):
    if request.method == 'POST':
        form = SubTareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recupera_tareas_y_sub_tareas')  # Redirige a la vista que muestra tareas y subtareas
    else:
        form = SubTareaForm()
    return render(request, 'crear_sub_tarea.html', {'form': form})



def elimina_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('recupera_tareas_y_sub_tareas')

def elimina_sub_tarea(request, subtarea_id):
    subtarea = get_object_or_404(SubTarea, id=subtarea_id)
    subtarea.delete()
    return redirect('recupera_tareas_y_sub_tareas')



def imprimir_en_pantalla(request):
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return render(request, 'imprimir_en_pantalla.html', {'tareas': tareas, 'subtareas': subtareas})

