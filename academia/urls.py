from django.urls import path
from . import views
from .views import MiLoginView

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('cursos/', views.ListaCursosView.as_view(), name='lista_cursos'),
    path('pagos/', views.AreaPagosView.as_view(), name='area_pagos'),
    path('inscribir/<int:curso_id>/', views.InscribirCursoView.as_view(), name='inscribir_curso'),
    path('mi-record/<int:pk>', views.RecordEstudianteView.as_view(), name='record_estudiante'),
    # ... tus otras rutas ...
    path('login/', views.MiLoginView.as_view(), name='login'),
    path('logout/', views.MiLogoutView.as_view(), name='logout'),
]
