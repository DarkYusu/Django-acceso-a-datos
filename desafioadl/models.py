from django.db import models

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')

    def __str__(self):
        return self.descripcion
