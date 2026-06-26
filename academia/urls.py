from django.urls import path
from . import views

urlpatterns = [
    # Cuando alguien entre a http://127.0.0.1:8000/ se ejecutará la vista 'lista_cursos'
    path('', views.ListaCursosView.as_view(), name='lista_cursos'),
]
