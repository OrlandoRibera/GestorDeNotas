# GestorDeNotas
Proyecto de Gestor de notas con roles de Alumnos, Docentes y Staff, desarrollado con Django

## APLICACIONES

  - Calificaciones
  - Core
  - Materias
  - Registration
  - Gestornotas
 
## MODELOS

  - Calificacion
  - Materia
  - User

## CARACTERÍSTICAS

  - Generic Views
  - User roles ( 'Docente', 'Alumnos' )
  - Forms
  
## Requisitos

### Proyecto

    $ pip install -r /path/to/requirements.txt
    
### Base de datos

  - Roles de Docente y Alumno
  
  * Docente:
    - Can see calificacion
    - Can update calificacion
    - Can delete calificacion
    - Can see materia
  * Alumno:
    - Can see materia
    - Can see calificacion
     
     
-Solo el staff podrá añadir usuarios
