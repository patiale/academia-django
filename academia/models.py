from django.db import models
from django.contrib.auth.models import User

# ==========================================
# 1. ESTRUCTURA DE CURSOS Y CONTENIDO
# ==========================================

class Curso(models.Model):
    NIVELES = [
        ('A1', 'Principiante (A1)'),
        ('A2', 'Elemental (A2)'),
        ('B1', 'Intermedio (B1)'),
        ('B2', 'Intermedio Alto (B2)'),
        ('C1', 'Avanzado (C1)'),
    ]
    nombre = models.CharField(max_length=150)
    nivel = models.CharField(max_length=10, choices=NIVELES, default='A1')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"


class ContenidoEducativo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    enlace_recurso = models.URLField(max_length=255, blank=True, null=True) 
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.curso.nombre} - {self.titulo}"


# ==========================================
# 2. PERFIL DE ESTUDIANTES Y GAMIFICACIÓN
# ==========================================

class PerfilEstudiante(models.Model):
    TIPOS_USUARIO = [
        ('Gratuito', 'Gratuito'),
        ('Premium', 'Premium'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    racha_dias = models.IntegerField(default=0)
    nivel_actual = models.CharField(max_length=10, default='A1')
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='Gratuito')
    cursos_comprados = models.TextField(blank=True, default="", help_text="IDs de cursos comprados separados por comas")

    def __str__(self):
        return f"Estudiante: {self.user.username} ({self.tipo_usuario})"


class ProgresoHabilidades(models.Model):
    estudiante = models.OneToOneField(PerfilEstudiante, on_delete=models.CASCADE, related_name='habilidades')
    listening_score = models.IntegerField(default=0)
    speaking_score = models.IntegerField(default=0)
    reading_score = models.IntegerField(default=0)
    writing_score = models.IntegerField(default=0)
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Habilidades de {self.estudiante.user.username}"


# ==========================================
# 3. PROFESORES Y CLASES EN VIVO
# ==========================================

class Profesor(models.Model):
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_completo


class ClaseEnVivo(models.Model):
    titulo_sesion = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='clases')
    fecha_hora_inicio = models.DateTimeField()
    nivel_sugerido = models.CharField(max_length=10, default='A1')
    url_zoom_meet = models.URLField(max_length=255)
    capacidad_maxima = models.IntegerField(default=15)

    def __str__(self):
        return f"{self.titulo_sesion} - {self.fecha_hora_inicio.strftime('%d/%m/%Y %H:%M')}"


class AsistenciaClaseVivo(models.Model):
    ESTADOS = [
        ('Reservado', 'Reservado'),
        ('Asistio', 'Asistió'),
        ('Falto', 'Faltó'),
    ]
    clase_vivo = models.ForeignKey(ClaseEnVivo, on_delete=models.CASCADE, related_name='asistencias')
    estudiante = models.ForeignKey(PerfilEstudiante, on_delete=models.CASCADE, related_name='asistencias_vivas')
    estado_reserva = models.CharField(max_length=20, choices=ESTADOS, default='Reservado')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('clase_vivo', 'estudiante')

    def __str__(self):
        return f"{self.estudiante.user.username} -> {self.clase_vivo.titulo_sesion}"


# ==========================================
# 4. CONTROL HISTÓRICO DE PAGOS
# ==========================================

class RegistroPago(models.Model):
    ESTADOS_PAGO = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado'),
        ('Fallido', 'Fallido'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='pagos')
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    referencia_transaccion = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='Pendiente')
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.referencia_transaccion} - {self.estado}"

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(PerfilEstudiante, on_delete=models.CASCADE, related_name='inscripciones_cursos')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes_inscritos')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    pago_verificado = models.BooleanField(default=False, verbose_name="Pago Verificado")

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = ('estudiante', 'curso') # Evita inscripciones duplicadas

    def __str__(self):
        return f"{self.estudiante.user.username} - {self.curso.nombre}"
    
class Inscripcion(models.Model):
    estudiante = models.ForeignKey(PerfilEstudiante, on_delete=models.CASCADE, related_name='inscripciones_cursos')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes_inscritos')
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    pago_verificado = models.BooleanField(default=False, verbose_name="Pago Verificado")

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        unique_together = ('estudiante', 'curso') # Evita inscripciones duplicadas

    def __str__(self):
        return f"{self.estudiante.user.username} - {self.curso.nombre}"