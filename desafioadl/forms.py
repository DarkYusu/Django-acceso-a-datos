from django import forms
from .models import Tarea, SubTarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['descripcion', 'eliminada']

class SubTareaForm(forms.ModelForm):
    class Meta:
        model = SubTarea
        fields = ['descripcion', 'eliminada', 'tarea']
