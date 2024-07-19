# Proyecto Django - myApp

Este repositorio contiene un proyecto Django llamado `myApp`, el cual incluye varias rutas y vistas para administrar cursos, profesores, estudiantes y entregables.

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_proyecto.git
   cd tu_proyecto

Crea y activa un entorno virtual (opcional pero recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # En Windows sería `venv\Scripts\activate`
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Configuración
Configura tu base de datos en settings.py:

python
Copiar código
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Ajusta la configuración de la base de datos según tus necesidades.

Realiza las migraciones iniciales:

bash
Copiar código
python manage.py migrate
Uso
URLs y Vistas
Inicio: /
Vista asociada: views.inicio
Cursos: /cursos/
Vista asociada: views.cursos
Profesores: /profesores/
Vista asociada: views.profesores
Estudiantes: /estudiantes/
Vista asociada: views.estudiantes
Entregables: /entregables/
Vista asociada: views.entregables
Crear Curso: /cursos/crear/
Vista asociada: views.cursosForm
Administración
Accede al panel de administración de Django con /admin/.

Contribución
Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Crea un pull request en GitHub.
Créditos
Desarrollado por Tu Nombre.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.