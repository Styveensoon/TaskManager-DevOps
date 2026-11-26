# Feature: edicion de tareas (RF03)

## Historia de usuario
Como usuario del sistema, quiero modificar la informacion de una tarea para mantenerla actualizada.

## Criterios de aceptacion
- El sistema permite editar nombre, descripcion, prioridad y estado.
- La edicion se refleja inmediatamente en el listado.
- Los campos no enviados conservan su valor anterior.
- Si el nombre queda vacio, el sistema responde 400 y conserva el nombre anterior.
- Si la tarea no existe, el sistema responde 404.

## Implementacion
- Endpoint `PUT /api/tareas/<id>`.
- El formulario cambia a modo edicion y el boton se muestra como "Actualizar tarea".
- El nombre se normaliza (se eliminan espacios) y no puede quedar vacio.
- La interfaz recarga el listado despues de guardar.

## Pruebas agregadas
`tests/test_editar_tareas.py`:
- Edicion de todos los campos.
- Edicion parcial que conserva los demas campos.
- Limpieza de espacios en el nombre.
- Nombre vacio devuelve 400 y conserva el nombre anterior.
- Edicion de una tarea inexistente devuelve 404.

## Issue relacionado
Implementar la edicion de tareas (#4).
