from django.contrib import admin
from .models import Curso, ContenidoEducativo, EstudiantePerfil, Nota, Pago

# Registramos cada modelo para que se dibuje en tu navegador
admin.site.register(Curso)
admin.site.register(ContenidoEducativo)
admin.site.register(EstudiantePerfil)
admin.site.register(Nota)
admin.site.register(Pago)
