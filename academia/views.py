from django.views.generic import ListView
from .models import Curso
from django.views.generic import TemplateView

class ListaCursosView(ListView):
    model = Curso
    template_name = 'academia/lista_cursos.html'  # El HTML que va a renderizar
    context_object_name = 'cursos'                # El nombre de la variable en el HTML

class InicioView(TemplateView):
    template_name = 'academia/inicio.html'