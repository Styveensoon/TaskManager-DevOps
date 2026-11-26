# Registro de Operacion y Monitoreo - TaskManager

**Fecha de monitoreo:** 25 de noviembre de 2026, 21:29 (hora local)
**Version monitoreada:** v1.0.0
**Aplicacion publicada:** https://styveensoon.github.io/TaskManager-DevOps/
**Repositorio:** https://github.com/Styveensoon/TaskManager-DevOps

## 1. Disponibilidad de la aplicacion publicada

| Verificacion | Resultado |
|--------------|-----------|
| Intento 1 | HTTP 200, 0.155 s, 11,148 bytes |
| Intento 2 | HTTP 200, 0.070 s, 11,148 bytes |
| Intento 3 | HTTP 200, 0.097 s, 11,148 bytes |
| Hoja de estilos `css/style.css` | HTTP 200, 0.156 s |

La pagina publicada responde correctamente y carga la interfaz funcional de TaskManager (no el README).

## 2. Tiempo de respuesta del backend (verificacion local)

El backend Flask + SQLite se ejecuto con gunicorn (`gunicorn app:app`) y una base temporal para las pruebas de monitoreo:

| Endpoint | Metodo | Codigo | Tiempo |
|----------|--------|--------|--------|
| `/api/health` | GET | 200 | 0.0031 s |
| `/api/tareas` | GET | 200 | 0.0010 s |
| `/api/tareas` | POST | 201 | 0.0017 s |
| `/api/tareas/1/estado` | PATCH | 200 | 0.0014 s |

Respuesta de salud:
```json
{"base_de_datos":"ok","hora":"2026-11-25T21:29:15.702117","status":"ok","total_tareas":0,"version":"1.0.0"}
```

El log de gunicorn no registro errores ni trazas durante las pruebas.

## 3. Correcto almacenamiento de la informacion

- En la version publicada (GitHub Pages), las tareas se almacenan en `localStorage` y persisten al recargar la pagina.
- En el backend Flask, SQLite guarda las tareas en `tasks.db`; las pruebas automatizadas usan una base temporal aislada.
- Se verifico crear, consultar, cambiar estado y eliminar tareas sin perdida de datos.

## 4. Funcionalidades principales verificadas

| Funcionalidad | Verificacion | Resultado |
|---------------|--------------|-----------|
| RF01 Registrar tareas | Formulario + `POST /api/tareas` | Correcto |
| RF02 Consultar tareas | Listado y `GET /api/tareas` | Correcto |
| RF03 Editar tareas | Formulario en modo edicion + `PUT` | Correcto |
| RF04 Eliminar tareas | Confirmacion + `DELETE` | Correcto |
| RF05 Cambiar estado | Boton de estado + `PATCH` | Correcto |
| RF06 Asignar prioridad | Selector Alta/Media/Baja | Correcto |

Evidencias visuales: `docs/01-inicio-vacio.png` a `docs/07-eliminar-tarea.png` y `docs/08-aplicacion-publicada.png` (pagina publicada).

## 5. Incidencias detectadas y atendidas

| Incidencia | Issue | Deteccion | Funcionalidad afectada | Causa | Solucion | Responsable | Estado |
|------------|-------|-----------|------------------------|-------|----------|-------------|--------|
| La pagina publicada mostraba el README | [#10](https://github.com/Styveensoon/TaskManager-DevOps/issues/10) | 25/11/2026 | Despliegue / GitHub Pages | La raiz de `gh-pages` no tenia `index.html` y Jekyll renderizaba el README | Workflow `pages.yml` publica `docs/` con la aplicacion funcional; Pages configurado con `build_type: workflow` | Ingeniero DevOps / QA | Corregida y verificada (HTTP 200 + captura) |
| Las pruebas contaminaban `tasks.db` | [#9](https://github.com/Styveensoon/TaskManager-DevOps/issues/9) | 25/11/2026 | Pruebas automatizadas | El fixture configuraba `app.config` pero `app.py` usaba una variable global | `get_db_connection()` usa `app.config['DB_PATH']`; fixture con `tmp_path` | Desarrollador 1 | Corregida (hash de `tasks.db` sin cambios) |
| Prueba de edicion esperaba 200 con nombre vacio | Run [#45747736075](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747736075) | 25/11/2026 | Edicion de tareas | Expectativa incorrecta de la prueba; el endpoint devuelve 400 correctamente | Se corrigio la prueba en el commit `49f17f5`; run exitoso [#45747763416](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747763416) | Desarrollador 2 | Corregida y CI en verde |

## 6. Propuestas de mejora para v2.0.0

Se registraron como Issues con el milestone `v2.0.0 - Mejoras`:

1. [Implementar autenticacion de usuarios (#11)](https://github.com/Styveensoon/TaskManager-DevOps/issues/11)
2. [Agregar filtros de busqueda y ordenamiento (#12)](https://github.com/Styveensoon/TaskManager-DevOps/issues/12)
3. [Incorporar notificaciones y reportes de productividad (#13)](https://github.com/Styveensoon/TaskManager-DevOps/issues/13)

## 7. Planeacion de la nueva version

| Actividad | Herramienta | Fase |
|-----------|-------------|------|
| Priorizar las mejoras del milestone v2.0.0 | GitHub Issues + Projects | Plan |
| Crear ramas `feature/auth`, `feature/busqueda`, `feature/reportes` | Git / GitHub | Code |
| Agregar pruebas para cada mejora | Pytest | Test |
| Ejecutar CI en cada Pull Request | GitHub Actions | CI |
| Publicar v2.0.0 y artefacto | Releases + Actions | Release |
| Medir disponibilidad y errores | `/api/health` + GitHub Issues | Operate / Monitor |

## 8. Conclusion

La aplicacion se encuentra disponible, responde en menos de 0.2 s en la pagina publicada y en menos de 5 ms en el backend local. Las funcionalidades RF01-RF06 fueron verificadas, las incidencias detectadas se corrigieron mediante ramas y Pull Requests, y las mejoras para la siguiente version quedaron planificadas en GitHub Issues con su milestone.
