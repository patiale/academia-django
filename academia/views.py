from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView, View

# Importamos tus modelos y formularios locales
from .models import Curso, Inscripcion, PerfilEstudiante
from .forms import RegistroPagoForm

# 1. VISTA DE INICIO
class InicioView(TemplateView):
    template_name = 'academia/inicio.html'

# 2. LISTA DE CURSOS
class ListaCursosView(ListView):
    model = Curso
    template_name = 'academia/lista_cursos.html'
    context_object_name = 'cursos'

# 3. REPORTAR UN PAGO
class AreaPagosView(CreateView):
    form_class = RegistroPagoForm
    template_name = 'academia/pagos/area_pagos.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        return super().form_valid(form)

# 4. PROCESAR INSCRIPCIÓN (Corregido get_object_or_404)
class InscribirCursoView(LoginRequiredMixin, View):
    def post(self, request, curso_id):
        curso = get_object_or_404(Curso, id=curso_id)
        
        # Buscamos el perfil del estudiante ligado al usuario actual
        perfil_estudiante = get_object_or_404(PerfilEstudiante, user=request.user)
        
        # Registramos la pre-inscripción si no existe ya
        inscripcion, creada = Inscripcion.objects.get_or_create(
            estudiante=perfil_estudiante,
            curso=curso
        )
        
        if creada:
            messages.success(request, f"¡Te has pre-inscrito con éxito en {curso.nombre}! Procede a realizar tu pago.")
        else:
            messages.info(request, f"Ya tienes una solicitud de inscripción en curso para {curso.nombre}.")
            
        return redirect('area_pagos')