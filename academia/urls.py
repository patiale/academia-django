from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('cursos/', views.ListaCursosView.as_view(), name='lista_cursos'),
    path('pagos/', views.AreaPagosView.as_view(), name='area_pagos'),
    path('inscribir/<int:curso_id>/', views.InscribirCursoView.as_view(), name='inscribir_curso'),
]