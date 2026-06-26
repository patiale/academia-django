from django.db import models
from django.contrib.auth.models import User

# 1. Cursos de Inglés
class Curso(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: Teens, Kids, Pre-K
    nivel = models.CharField(max_length=50)   # Ej: Beginner, A2, B1
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"

# 2. Contenido Educativo por Curso
class ContenidoEducativo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='contenidos')
    titulo = models.CharField(max_length=200)   # Ej: Vocabulario para Spelling Bee
    descripcion = models.TextField()
    enlace_recurso = models.URLField(blank=True, null=True) # Para links de Drive, Canva, etc.
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.curso.nombre}"

# 3. Perfil de los Estudiantes
class EstudiantePerfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso_asignado = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

# 4. Control de Notas
class Nota(models.Model):
    estudiante = models.ForeignKey(EstudiantePerfil, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    evaluacion = models.CharField(max_length=100) # Ej: Primer Parcial, Spelling Bee Contest
    calificacion = models.DecimalField(max_digits=5, decimal_places=2) 
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.estudiante.user.username} - {self.evaluacion}: {self.calificacion}"

# 5. Control de Pagos
class Pago(models.Model):
    ESTATUS_CHOICES = [
        ('PE', 'Pendiente'),
        ('AP', 'Aprobado'),
        ('RE', 'Rechazado'),
    ]
    estudiante = models.ForeignKey(EstudiantePerfil, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    referencia_transaccion = models.CharField(max_length=100, unique=True)
    fecha_pago = models.DateField()
    estatus = models.CharField(max_length=2, choices=ESTATUS_CHOICES, default='PE')
    comprobante_captura = models.ImageField(upload_to='pagos/', blank=True, null=True) 

    def __str__(self):
        return f"Pago {self.referencia_transaccion} - {self.estudiante.user.username} ({self.get_estatus_display()})"
