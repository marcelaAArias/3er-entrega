from django import forms

class FormularioCurso(forms.form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()