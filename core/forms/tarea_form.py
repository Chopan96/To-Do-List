from ..models import Tarea
from django import forms

class TareaForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields=['nombre', 'descripcion']