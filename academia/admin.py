from django.contrib import admin
from django.contrib import admin
from .models import (
    Curso, 
    ContenidoEducativo, 
    PerfilEstudiante, 
    ProgresoHabilidades, 
    Profesor, 
    ClaseEnVivo, 
    AsistenciaClaseVivo, 
    RegistroPago,
    Inscripcion
)

# Registramos cada modelo una única vez
admin.site.register(Curso)
admin.site.register(ContenidoEducativo)
admin.site.register(PerfilEstudiante)
admin.site.register(ProgresoHabilidades)
admin.site.register(Profesor)
admin.site.register(ClaseEnVivo)
admin.site.register(AsistenciaClaseVivo)
admin.site.register(RegistroPago)
admin.site.register(Inscripcion)