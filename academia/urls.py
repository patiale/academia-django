from django.urls import path
from . import views
from .views import ListaClasesEnVivoView

urlpatterns = [
    # Rutas principales de la academia
    path('', views.InicioView.as_view(), name='inicio'),
    path('cursos/', views.ListaCursosView.as_view(), name='lista_cursos'),
    path('pagos/', views.AreaPagosView.as_view(), name='area_pagos'),
    path('inscribir/<int:curso_id>/', views.InscribirCursoView.as_view(), name='inscribir_curso'),
    path('mi-record/<int:pk>/', views.RecordEstudianteView.as_view(), name='record_estudiante'),
    
    # Autenticación (Usando tus vistas personalizadas)
    #path('', views.MiLoginView.as_view(), name='login'),
    path('logout/', views.MiLogoutView.as_view(), name='logout'),
    path('clases-en-vivo/', ListaClasesEnVivoView.as_view(), name='clases_en_vivo'),
]