from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)
    result = []
    for tarea in tareas:
        subtareas = tarea.subtareas.filter(eliminada=False)
        result.append({
            'tarea': tarea,
            'subtareas': subtareas
        })
    return result

def crear_nueva_tarea(descripcion):
    Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas_subtareas):
    for item in tareas_subtareas:
        tarea = item['tarea']
        subtareas = item['subtareas']
        print(f'[{tarea.id}] {tarea.descripcion}')
        for subtarea in subtareas:
            print(f'.... [{subtarea.id}] {subtarea.descripcion}')
