from django.shortcuts import render
from .models import Tarea
from .forms import TareaForm
from django.http import HttpResponseRedirect

def home(request):
    if request.method== 'POST':
        if 'save' in request.POST:
            form = TareaForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'delete' in request.POST:
            pk=request.POST.get('delete')
            tarea=Tarea.objects.get(pk=pk)
            tarea.delete()
        return HttpResponseRedirect(request.path_info) 
            
    tareas=Tarea.objects.all()
    form = TareaForm()
    return render(request,'home.html',{'tareas':tareas,'form':form})