erDiagram
    %% 1. Cursos de Inglés
    Curso {
        int id PK
        string nombre
        string nivel
        text descripcion
    }

    %% 2. Contenido Educativo por Curso
    ContenidoEducativo {
        int id PK
        int curso_id FK
        string titulo
        text descripcion
        string enlace_recurso
        date fecha_creacion
    }

    %% 3. Perfil de los Estudiantes
    EstudiantePerfil {
        int id PK
        int user_id FK
        int curso_asignado_id FK
        string telefono
    }

    %% 4. Control de Notas
    Nota {
        int id PK
        int estudiante_id FK
        int curso_id FK
        string evaluacion
        decimal calificacion
        text observaciones
    }

    %% 5. Control de Pagos
    Pago {
        int id PK
        int estudiante_id FK
        decimal monto
        string referencia_transaccion
        date fecha_pago
        string estatus
        string comprobante_captura
    }

    %% Relaciones basadas en tus modelos de Django
    Curso ||--o{ ContenidoEducativo : "tiene (1:N)"
    Curso ||--o{ EstudiantePerfil : "asigna (1:N)"
    Curso ||--o{ Nota : "evalúa (1:N)"
    EstudiantePerfil ||--o{ Nota : "recibe (1:N)"
    EstudiantePerfil ||--o{ Pago : "realiza (1:N)"