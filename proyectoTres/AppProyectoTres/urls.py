
from django.urls import path
from AppProyectoTres import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('form-con-api/', views.form_con_api, name="FormConApi")
]