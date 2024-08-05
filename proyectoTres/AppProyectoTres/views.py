from django.shortcuts import render
from django.http import HttpResponse

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






