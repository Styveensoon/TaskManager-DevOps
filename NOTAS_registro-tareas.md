# Feature: registro de tareas (RF01)

## Historia de usuario
Como usuario del sistema, quiero registrar nuevas tareas para organizar mis actividades.

## Criterios de aceptacion
- El sistema permite ingresar el nombre de la tarea.
- El sistema permite agregar una descripcion.
- El sistema permite seleccionar una prioridad (Alta, Media, Baja).
- El sistema guarda la tarea en SQLite.
- El sistema muestra un mensaje de confirmacion y la tarea aparece en el listado.

## Implementacion
- Endpoint `POST /api/tareas`.
- Validacion: el nombre es obligatorio (HTTP 400 si esta vacio).
- Normalizacion: se eliminan espacios al inicio y al final del nombre.
- Prioridad por defecto: Media. Estado por defecto: Pendiente.
- Interfaz: formulario "Nueva tarea" en `templates/index.html` y `static/js/app.js`.

## Pruebas agregadas
`tests/test_registro_tareas.py`:
- Registro completo con nombre, descripcion, prioridad y estado.
- Limpieza de espacios en el nombre.
- La tarea creada aparece en el listado.
- Solicitud sin cuerpo JSON devuelve validacion 400.

## Issue relacionado
Implementar el registro de tareas (#3).
