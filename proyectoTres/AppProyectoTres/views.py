from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "Appproyecto2/index.html")

def cursos(request):
    return render(request, "templates/Appproyecto2/cursos.html")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")






