from django import forms 


class cursoFormulario(forms.Form) :
    Cursos = forms.CharField()
    Camada = forms.IntegerField()

