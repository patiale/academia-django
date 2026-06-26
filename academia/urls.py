from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('cursos/', views.ListaCursosView.as_view(), name='lista_cursos'),
]