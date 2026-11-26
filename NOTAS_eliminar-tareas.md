# Feature: eliminacion de tareas (RF04)

## Historia de usuario
Como usuario del sistema, quiero eliminar tareas existentes para mantener limpio el listado.

## Criterios de aceptacion
- El sistema solicita confirmacion antes de eliminar.
- La tarea desaparece del listado despues de eliminarla.
- Solo se elimina la tarea seleccionada.
- Si la tarea no existe, el sistema responde 404.

## Implementacion
- Endpoint `DELETE /api/tareas/<id>`.
- Confirmacion en la interfaz con `confirm()`.
- El listado se recarga automaticamente tras la eliminacion.
- Respuesta JSON `{"ok": true, "mensaje": "Tarea eliminada"}`.

## Pruebas agregadas
`tests/test_eliminar_tareas.py`:
- La tarea eliminada desaparece del listado.
- Solo se elimina la tarea seleccionada.
- Consultar una tarea eliminada devuelve 404.
- Eliminar una tarea inexistente devuelve 404.

## Issue relacionado
Cierre del requerimiento RF04 dentro de la fase de Desarrollo.
