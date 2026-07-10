from django.contrib import admin
from django.urls import path, include
# Importa tu vista de login desde la aplicación 'academia'
from academia.views import MiLoginView 

urlpatterns = [
    # 1. Acceso al panel de administración
    path('admin/', admin.site.urls),
    
    # 2. Página inicial (la raíz '' ahora es el login)
    path('', MiLoginView.as_view(), name='login'),
    
    # 3. Resto de las rutas de tu aplicación bajo el prefijo 'academia/'
    path('academia/', include('academia.urls')),
]