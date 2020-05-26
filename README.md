# GestorDeNotas
Proyecto de Gestor de notas con roles de Alumnos, Docentes y Staff, desarrollado con Django

APPS
----

  - Calificaciones
  - Core
  - Materias
  - Registration
  - Gestornotas
 
MODELS
------

  - Calificacion
  - Materia
  - User

FEATURES
--------

  - Generic Views
  - User roles ( 'Docente', 'Alumnos' )
  - Forms
  
Requisitos del proyecto
-----------------------

    $ pip install -r /path/to/requirements.txt
    
Requisitos en DB
----------------
  - Roles de Docente y Alumno
  
  * Docente:
    - Can see calificacion
    - Can update calificacion
    - Can delete calificacion
    - Can see materia
  * Alumno:
    - Can see materia
    - Can see calificacion
     
     
* Solo el staff podrá añadir usuarios
