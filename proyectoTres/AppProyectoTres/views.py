from django.shortcuts import render
from AppProyectoTres.forms import cursoFormulario
#from django.http import HttpResponse
from AppProyectoTres.models import Curso

def inicio(request):
    return render(request,"AppProyectoTres/index.html")

def cursos(request):
    return render(request,"AppProyectoTres/curso.html")

def profesores(request):
    return render(request, "AppProyectoTres/profesores.html")

def estudiantes(request):
    return render(request,"AppProyectoTres/estudiantes.html")

def entregables(request):
    return render(request,"AppProyectoTres/entregables.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = cursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            curso = Curso(nombre=informacion["Cursos"], Camada=informacion["Camada"])
            curso.save()

            return render(request,"AppProyectoTres/index.html")
        else:
            # Si el formulario no es válido, se renderiza de nuevo con el formulario
            return render(request, "AppProyectoTres/form_con_api.html", {"mi_formulario": mi_formulario})
        
    else:
        mi_formulario = cursoFormulario()

    return render(request, "AppProyectoTres/form_con_api.html", {"mi_formulario": mi_formulario})


