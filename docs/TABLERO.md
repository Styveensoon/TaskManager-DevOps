# Tablero de trabajo - TaskManager DevOps

Respaldo de la planificacion del tablero Kanban de GitHub Projects. Columnas: **Backlog**, **To Do**, **In Progress**, **Review**, **Done**.

| Backlog | To Do | In Progress | Review | Done |
|---------|-------|-------------|--------|------|
| Mejora v2.0.0: notificaciones y reportes (#13) | Mejora v2.0.0: autenticacion (#11) | - | - | Estructura inicial (#1) |
| Mejora v2.0.0: busqueda y filtros (#12) | - | - | - | Interfaz del sistema (#2) |
| - | - | - | - | Registro de tareas (#3) |
| - | - | - | - | Edicion de tareas (#4) |
| - | - | - | - | Pruebas unitarias (#5) |
| - | - | - | - | Eliminacion de tareas (#16) |
| - | - | - | - | Cambio de estado (#17) |
| - | - | - | - | Prioridad (#18) |
| - | - | - | - | Incidencia: README en Pages (#10) |
| - | - | - | - | Incidencia: pruebas contaminan la BD (#9) |

## Flujo de trabajo

1. Las actividades se registran como Issues con prioridad, estimacion, fase DevOps y fecha limite.
2. Al iniciar el trabajo, el Issue pasa de `To Do` a `In Progress`.
3. Al abrir el Pull Request, pasa a `Review`; la CI debe estar en verde.
4. Al fusionar el PR y cerrar el Issue, pasa a `Done`.
5. Las mejoras sin fecha de inicio permanecen en `Backlog` con el milestone `v2.0.0 - Mejoras`.

## Enlaces

- GitHub Projects: https://github.com/users/Styveensoon/projects/1
- Issues: https://github.com/Styveensoon/TaskManager-DevOps/issues
- Milestone v2.0.0: https://github.com/Styveensoon/TaskManager-DevOps/milestone/1
