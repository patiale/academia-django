from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView, View

# Importamos tus modelos y formularios locales
from .models import Curso, Inscripcion, PerfilEstudiante
from .forms import RegistroPagoForm

from django.contrib.auth.views import LoginView, LogoutView

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

# 4. PROCESAR INSCRIPCIÓN
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
    
# 5. RÉCORD ACADÉMICO DEL ESTUDIANTE
class RecordEstudianteView(LoginRequiredMixin, ListView):
    model = PerfilEstudiante
    template_name = 'academia/record_estudiante.html'
    context_object_name = 'inscripciones'

    def get_queryset(self):
        # Buscamos el perfil del estudiante logueado actual
        perfil = get_object_or_404(PerfilEstudiante, user=self.request.user)
        # Filtramos para mostrar únicamente las inscripciones de este alumno
        return Inscripcion.objects.filter(estudiante=perfil).order_by('-fecha_inscripcion')
    
# 6. LOGIN DE USUARIOS
class MiLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = False
    
    def get_success_url(self):
        return reverse_lazy('inicio')

# 7. LOGOUT DE USUARIOS (Muestra tu plantilla de despedida)
class MiLogoutView(LogoutView):
    template_name = 'logout.html'