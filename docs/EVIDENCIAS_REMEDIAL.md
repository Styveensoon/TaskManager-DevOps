# Evidencias del Remedial - TaskManager DevOps

Documento de resultados, evidencias y conclusiones de las 7 fases de DevOps solicitadas en `Remedial.md`.

## Datos del proyecto

| Dato | Valor |
|------|-------|
| Repositorio | https://github.com/Styveensoon/TaskManager-DevOps |
| Aplicacion publicada | **https://styveensoon.github.io/TaskManager-DevOps/** |
| Version | v1.0.0 |
| Stack | Flask + SQLite + HTML/CSS/JavaScript |
| Pruebas | 26 pruebas automatizadas con Pytest |
| CI | GitHub Actions - `Integracion Continua` |
| CD | GitHub Actions - `Entrega Continua` y `Desplegar aplicacion en GitHub Pages` |
| Documento de monitoreo | [MONITOREO.md](MONITOREO.md) |

> **Importante:** la URL publica muestra la **aplicacion funcional** de TaskManager, no el README. El despliegue se hace con `.github/workflows/pages.yml` sobre la carpeta `docs/`, verificada con HTTP 200 y captura de pantalla.

---

## Fase 1. Planificacion (Plan)

**Objetivo:** organizar el proyecto, identificar requerimientos y distribuir actividades.

### Actividad 1 - Repositorio en GitHub
- Repositorio publico `TaskManager-DevOps`.
- Descripcion: "Sistema web para la gestion de tareas."
- README inicial activado y actualizado con instrucciones, URL publica y enlaces.
- URL: https://github.com/Styveensoon/TaskManager-DevOps

### Actividad 2 - Tablero GitHub Projects
- Tablero Kanban con las columnas: `Backlog`, `To Do`, `In Progress`, `Review`, `Done`.
- Los Issues se clasificaron con etiquetas de estado, prioridad y fase DevOps.
- Enlace del tablero: https://github.com/users/Styveensoon/projects/1

> Si el tablero no carga sin iniciar sesion, el repositorio conserva la misma planificacion en Issues, etiquetas y en el archivo [TABLERO.md](TABLERO.md).

### Actividad 3 - Historias de usuario

**HU1 - Registrar tareas**
> Como usuario del sistema, quiero registrar nuevas tareas para organizar mis actividades.

Criterios de aceptacion:
- Ingresar el nombre de la tarea.
- Agregar una descripcion.
- Seleccionar una prioridad (Alta, Media, Baja).
- Guardar la tarea.
- Mostrar un mensaje de confirmacion y reflejarla en el listado.

**HU2 - Cambiar estado de tareas**
> Como usuario, quiero cambiar el estado de una tarea para conocer su progreso.

Criterios de aceptacion:
- Seleccionar Pendiente, En Proceso o Terminada.
- El cambio se refleja en el listado.
- Un estado invalido se rechaza.

**HU3 - Consultar tareas:** como usuario quiero ver todas las tareas registradas y filtrarlas por estado.

**HU4 - Editar tareas:** como usuario quiero modificar nombre, descripcion, prioridad y estado de una tarea.

**HU5 - Eliminar tareas:** como usuario quiero eliminar tareas existentes con confirmacion.

**HU6 - Asignar prioridad:** como usuario quiero clasificar tareas como Alta, Media o Baja y verla con color.

### Actividad 4 - Issues y propiedades

| Issue | Titulo | Estado | Prioridad | Fase DevOps | Evidencia |
|-------|--------|--------|-----------|-------------|-----------|
| [#1](https://github.com/Styveensoon/TaskManager-DevOps/issues/1) | Crear la estructura inicial del proyecto | Done | Alta | Plan | Commit `324d562` |
| [#2](https://github.com/Styveensoon/TaskManager-DevOps/issues/2) | Disenar la interfaz del sistema | Done | Media | Code | `templates/` y `static/` |
| [#3](https://github.com/Styveensoon/TaskManager-DevOps/issues/3) | Implementar el registro de tareas | Done | Alta | Code | PR #6 |
| [#4](https://github.com/Styveensoon/TaskManager-DevOps/issues/4) | Implementar la edicion de tareas | Done | Media | Code | PR #7 |
| [#5](https://github.com/Styveensoon/TaskManager-DevOps/issues/5) | Implementar las pruebas unitarias | Done | Alta | Test | 26 pruebas |
| [#16](https://github.com/Styveensoon/TaskManager-DevOps/issues/16) | Implementar la eliminacion de tareas (RF04) | Done | Alta | Code | PR #8 |
| [#17](https://github.com/Styveensoon/TaskManager-DevOps/issues/17) | Implementar el cambio de estado (RF05) | Done | Media | Code | `test_cambiar_estado` |
| [#18](https://github.com/Styveensoon/TaskManager-DevOps/issues/18) | Implementar la prioridad (RF06) | Done | Media | Code | `test_seleccionar_prioridad` |

Propiedades usadas en los Issues: titulo, responsable, estado, prioridad, estimacion, fase DevOps y fecha limite (cuando aplica). Se usaron etiquetas `Backlog`, `To Do`, `In Progress`, `Done`, `Critica/Alta/Media/Baja` y `Plan/Code/Build/Test/Release/Deploy/Operate/Monitor`.

### Evidencias Fase 1
- Repositorio creado y publico.
- Tablero de GitHub Projects con 5 columnas.
- Historias de usuario HU1-HU6.
- 13 Issues creados y atendidos (10 cerrados y 3 mejoras abiertas para v2.0.0).
- Distribucion de responsabilidades (ver seccion Equipo).

---

## Fase 2. Desarrollo (Code)

El codigo fuente se desarrollo con Git y GitHub, usando ramas por funcionalidad y Pull Requests revisados.

### Estructura del proyecto (Flask + SQLite)
```
TaskManager-DevOps/
├── app.py
├── requirements.txt
├── README.md
├── templates/index.html
├── static/css/style.css
├── static/js/app.js
├── tests/
│   ├── conftest.py
│   ├── test_app.py
│   ├── test_registro_tareas.py
│   ├── test_editar_tareas.py
│   └── test_eliminar_tareas.py
├── docs/                       # sitio publicado + evidencias
│   ├── index.html
│   ├── css/style.css
│   ├── js/app.js
│   ├── EVIDENCIAS_REMEDIAL.md
│   └── MONITOREO.md
└── .github/workflows/
    ├── ci.yml
    ├── cd.yml
    └── pages.yml
```

### Ramas de desarrollo
| Rama | Funcionalidad | Pull Request | Estado |
|------|---------------|--------------|--------|
| `feature/registro-tareas` | RF01 Registrar tareas | [#6](https://github.com/Styveensoon/TaskManager-DevOps/pull/6) | Fusionado |
| `feature/editar-tareas` | RF03 Editar tareas | [#7](https://github.com/Styveensoon/TaskManager-DevOps/pull/7) | Fusionado |
| `feature/eliminar-tareas` | RF04 Eliminar tareas | [#8](https://github.com/Styveensoon/TaskManager-DevOps/pull/8) | Fusionado |
| `fix/aislamiento-db-y-salud` | Correccion de pruebas + health | [#14](https://github.com/Styveensoon/TaskManager-DevOps/pull/14) | Fusionado |
| `ci/despliegue-pages-funcional` | Despliegue funcional en Pages | [#15](https://github.com/Styveensoon/TaskManager-DevOps/pull/15) | Fusionado |

### Commits representativos
```text
c90a7d3 Merge pull request #8 from Styveensoon/feature/eliminar-tareas
3db9e00 Merge pull request #7 from Styveensoon/feature/editar-tareas
b997691 Merge pull request #6 from Styveensoon/feature/registro-tareas
5f10550 Merge pull request #15 from Styveensoon/ci/despliegue-pages-funcional
f998280 Merge pull request #14 from Styveensoon/fix/aislamiento-db-y-salud
e1bcd54 fix(test): aislar base de datos de pruebas y agregar endpoint de salud
49f17f5 fix(test): corregir expectativa de validacion al editar con nombre vacio
```

### Revisiones y Pull Requests
Cada PR incluye descripcion, criterios de aceptacion, evidencia de CI y un comentario de revision. Se aprobaron y fusionaron a `main` cuando el workflow `Integracion Continua` quedo en verde.

### Evidencias Fase 2
- Codigo fuente con el 100% de RF01-RF06.
- 5 ramas fusionadas mediante Pull Requests.
- Commits e historial en GitHub.
- Revisiones registradas en cada PR.
- Captura de la lista de Pull Requests: `docs/evidencias-github/10-pull-requests.png`.

---

## Fase 3. Integracion continua (CI)

### Pruebas unitarias y de integracion
Archivo principal: `tests/test_app.py`, complementado con pruebas por funcionalidad. Se usa el cliente de pruebas de Flask y una base SQLite temporal (`tmp_path`) para no contaminar `tasks.db`.

Resultado local:
```text
============================= test session starts ==============================
platform linux -- Python 3.13.18, pytest-9.2.0
collected 26 items
...
============================== 26 passed in 0.10s ==============================
```

### Archivo de automatizacion
`.github/workflows/ci.yml` se ejecuta en cada `push` a `main` y en cada `pull_request` hacia `main`:
- Descarga el codigo (`actions/checkout@v4`).
- Configura Python 3.12 (`actions/setup-python@v5`).
- Instala dependencias (`pip install -r requirements.txt`).
- Ejecuta `PYTHONPATH=. pytest`.

### Ejecuciones en GitHub Actions
| Run | Descripcion | Resultado |
|-----|-------------|-----------|
| [#45747915314](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747915314) | CI en `main` despues del ultimo merge | Exitoso |
| [#45747637553](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747637553) | CI del PR #6 | Exitoso |
| [#45747763416](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747763416) | CI del PR #7 corregido | Exitoso |
| [#45747867964](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747867964) | CI del PR #8 | Exitoso |
| [#45747736075](https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747736075) | Error detectado en la prueba de edicion | Fallido y corregido |

### Evidencias Fase 3
- `ci.yml` versionado.
- 26 pruebas automatizadas.
- Ejecuciones exitosas en Actions.
- Captura de workflows: `docs/evidencias-github/11-github-actions.png`.
- Registro del error detectado y corregido (seccion Fase 4).

---

## Fase 4. Pruebas (Test)

### Matriz de casos de prueba

| ID | Prueba | Resultado esperado | Resultado obtenido | Automatizacion |
|----|--------|--------------------|--------------------|----------------|
| CP01 | Registrar una tarea | La tarea se guarda correctamente | OK (201) | `test_registro_tarea` |
| CP02 | Registrar tarea sin nombre | El sistema muestra una validacion | OK (400) | `test_registro_tarea_sin_nombre` |
| CP03 | Consultar tareas | Se muestra el listado | OK (200) | `test_consultar_tareas` |
| CP04 | Editar una tarea | Se actualiza la informacion | OK (200) | `test_editar_tarea` |
| CP05 | Eliminar una tarea | La tarea desaparece del listado | OK (200) | `test_eliminar_tarea` |
| CP06 | Cambiar estado | Se actualiza el estado | OK (200) | `test_cambiar_estado` |
| CP07 | Seleccionar prioridad | Se guarda la prioridad elegida | OK (201) | `test_seleccionar_prioridad` |
| CP08 | Monitoreo / salud | El endpoint responde `status: ok` | OK (200) | `test_health` |

Pruebas adicionales: prioridad invalida, estado invalido, editar/eliminar tarea inexistente, registro sin JSON, edicion parcial y conservacion de campos.

### Pruebas funcionales manuales
1. Abrir https://styveensoon.github.io/TaskManager-DevOps/.
2. Registrar "Elaborar documentacion" con prioridad Alta.
3. Verificar que aparece en el listado y el mensaje de confirmacion.
4. Cambiar el estado de Pendiente a En Proceso y luego a Terminada.
5. Editar nombre, descripcion y prioridad.
6. Filtrar por estado.
7. Eliminar una tarea y verificar que desaparece.

Resultado: todas las funcionalidades responden correctamente. Evidencias: capturas `01` a `07` y `08-aplicacion-publicada.png`.

### Errores reportados mediante Issues

**Issue #9 - Las pruebas escriben en `tasks.db`**
- Funcionalidad afectada: pruebas automatizadas.
- Pasos: ejecutar `pytest` y abrir la aplicacion.
- Resultado obtenido: aparecian tareas de prueba en la base real.
- Resultado esperado: base temporal aislada.
- Prioridad: Alta.
- Correccion: PR #14, fixture con `tmp_path`, `app.config['DB_PATH']` y verificacion del hash de `tasks.db`.
- Evidencia: hash identico antes y despues de pytest.

**Issue #10 - GitHub Pages mostraba el README**
- Funcionalidad afectada: despliegue.
- Pasos: abrir la URL publica.
- Resultado obtenido: se renderizaba el README.
- Resultado esperado: interfaz funcional.
- Prioridad: Alta.
- Correccion: PR #15, workflow `pages.yml`, `docs/index.html` y `build_type: workflow`.
- Evidencia: HTTP 200 + captura `08-aplicacion-publicada.png`.

**Error detectado por CI en el PR #7**
- La prueba esperaba HTTP 200 al editar con nombre vacio; el endpoint devolvia 400 correctamente.
- Correccion en el commit `49f17f5`.
- Run fallido: #45747736075; run exitoso: #45747763416.

### Evidencias Fase 4
- Matriz de casos de prueba (arriba).
- 26/26 pruebas aprobadas.
- Issues #9 y #10 cerrados con su correccion.
- Capturas funcionales en `docs/`.
- Nueva ejecucion exitosa de GitHub Actions.

---

## Fase 5. Entrega continua (Continuous Delivery)

### Version estable
Se verifico:
- RF01-RF06 implementadas.
- 26 pruebas aprobadas.
- Sin errores criticos conocidos.
- Codigo integrado en `main`.
- Documentacion completa (README, evidencias y monitoreo).

### Release
- Etiqueta: `v1.0.0`
- Titulo: **Primera version estable de TaskManager**
- URL: https://github.com/Styveensoon/TaskManager-DevOps/releases/tag/v1.0.0
- Notas de version: funcionalidades RF01-RF06, 26 pruebas, CI/CD y URL publica.
- Captura: `docs/evidencias-github/12-release-v1.0.0.png`.

### Automatizacion de entrega
`.github/workflows/cd.yml` se ejecuta al publicar un release y genera el artefacto `TaskManager-v1` con `app.py`, `requirements.txt`, `templates/`, `static/` y `README.md`.

| Evidencia | Detalle |
|-----------|---------|
| Workflow | `.github/workflows/cd.yml` |
| Artefacto | `TaskManager-v1` |
| Run de entrega | https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45447470673 |
| Tamano del artefacto | ~7.4 KB (comprimido) |

### Evidencias Fase 5
- Version estable v1.0.0.
- Release publicado con notas.
- Workflow de entrega.
- Artefacto descargable generado.
- Capturas del release.

---

## Fase 6. Despliegue continuo (Continuous Deployment)

### Plataforma seleccionada
**GitHub Pages** para publicar la version funcional estatica de TaskManager (frontend con `localStorage`). El backend Flask + SQLite se mantiene en el repositorio y puede desplegarse en Render/Railway/Fly.io con `gunicorn app:app`.

### Configuracion del despliegue
- Workflow: `.github/workflows/pages.yml`.
- Fuente: carpeta `docs/`.
- Acciones: `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`.
- GitHub Pages configurado con `build_type: workflow`.
- Entorno `github-pages` con politica de rama `main`.
- URL publica: **https://styveensoon.github.io/TaskManager-DevOps/**

### Verificacion de la aplicacion publicada
| Verificacion | Resultado |
|--------------|-----------|
| URL accesible | HTTP 200 |
| Pagina principal carga | Correcto (titulo TaskManager) |
| Registrar tareas | Correcto |
| Consultar tareas | Correcto |
| Editar tareas | Correcto |
| Eliminar tareas | Correcto |
| Cambiar estado | Correcto |
| Filtrar por estado | Correcto |
| Tiempo de respuesta | 0.070 s - 0.156 s |

### Evidencias Fase 6
- Workflow de despliegue exitoso: https://github.com/Styveensoon/TaskManager-DevOps/actions/runs/45747915482
- URL publica del sistema.
- Captura de la pagina publicada: `docs/evidencias-github/08-aplicacion-publicada.png`.
- Capturas de la aplicacion funcionando: `docs/01-*.png` a `docs/07-*.png`.

---

## Fase 7. Operacion y monitoreo (Operate & Monitor)

### Monitoreo
Se verifico disponibilidad, tiempo de respuesta, errores, almacenamiento y funcionalidades principales. El detalle completo esta en [MONITOREO.md](MONITOREO.md).

| Indicador | Resultado |
|-----------|-----------|
| Disponibilidad de la pagina publicada | 3/3 intentos HTTP 200 |
| Tiempo de respuesta de la pagina | 0.070 s - 0.156 s |
| Tiempo de respuesta del backend | 0.001 s - 0.003 s |
| Endpoint de salud | `/api/health` -> `status: ok` |
| Errores en el log de gunicorn | 0 |
| Almacenamiento | SQLite / localStorage verificado |

### Registro de incidencias
| Incidencia | Issue | Responsable | Solucion | Estado |
|------------|-------|-------------|----------|--------|
| Pagina publicada mostraba README | [#10](https://github.com/Styveensoon/TaskManager-DevOps/issues/10) | Ingeniero DevOps / QA | Workflow de Pages + `docs/index.html` | Cerrada |
| Pruebas contaminaban base real | [#9](https://github.com/Styveensoon/TaskManager-DevOps/issues/9) | Desarrollador 1 | `tmp_path` + `app.config['DB_PATH']` | Cerrada |
| Prueba de edicion con expectativa incorrecta | Run #45747736075 | Desarrollador 2 | Correccion de la prueba | Cerrada |

### Propuestas de mejora (v2.0.0)
1. Autenticacion de usuarios con roles - Issue [#11](https://github.com/Styveensoon/TaskManager-DevOps/issues/11).
2. Busqueda, filtros combinados y ordenamiento - Issue [#12](https://github.com/Styveensoon/TaskManager-DevOps/issues/12).
3. Notificaciones y reportes de productividad - Issue [#13](https://github.com/Styveensoon/TaskManager-DevOps/issues/13).

Las tres mejoras estan asociadas al milestone `v2.0.0 - Mejoras`, con prioridad y fase DevOps definidas.

### Evidencias Fase 7
- Registro de monitoreo con metricas reales.
- Incidencias documentadas y cerradas.
- Propuestas de mejora con Issues.
- Planeacion de la nueva version.

---

## Capturas de pantalla

| Archivo | Descripcion |
|---------|-------------|
| `docs/01-inicio-vacio.png` | Pantalla inicial sin tareas (RF02). |
| `docs/02-despues-registrar.png` | Tarea registrada con mensaje de confirmacion (RF01). |
| `docs/03-dos-tareas.png` | Dos tareas con distinta prioridad y estado. |
| `docs/04-cambiar-estado.png` | Cambio de estado Pendiente -> En Proceso (RF05). |
| `docs/05-filtro-terminada.png` | Filtro por estado Terminada. |
| `docs/06-editar-tarea.png` | Edicion de una tarea existente (RF03). |
| `docs/07-eliminar-tarea.png` | Tarea eliminada y listado actualizado (RF04). |
| `docs/evidencias-github/08-aplicacion-publicada.png` | URL publica funcionando. |
| `docs/evidencias-github/09-issues.png` | Issues creados y atendidos. |
| `docs/evidencias-github/10-pull-requests.png` | Pull Requests fusionados con CI en verde. |
| `docs/evidencias-github/11-github-actions.png` | Ejecuciones de GitHub Actions. |
| `docs/evidencias-github/12-release-v1.0.0.png` | Release v1.0.0 publicado. |

---

## Equipo y distribucion de responsabilidades

| Rol | Integrante | Responsabilidades |
|-----|------------|-------------------|
| Product Owner | Equipo TaskManager | Requerimientos, historias de usuario y prioridades. |
| Desarrollador 1 | Equipo TaskManager | Backend Flask, SQLite y funcionalidades principales. |
| Desarrollador 2 | Equipo TaskManager | Interfaz, estilos, JavaScript y funcionalidades adicionales. |
| Ingeniero DevOps / QA | Equipo TaskManager | CI/CD, pruebas, despliegue y monitoreo. |

Todos los integrantes participaron en revisiones de codigo, pruebas y conocimiento de las fases DevOps.

---

## Entregables del proyecto

1. URL del repositorio: https://github.com/Styveensoon/TaskManager-DevOps
2. Tablero de GitHub Projects: https://github.com/users/Styveensoon/projects/1
3. Historias de usuario HU1-HU6.
4. Issues creados y atendidos: 13 Issues.
5. Codigo fuente completo.
6. Ramas y Pull Requests: PR #6, #7, #8, #14 y #15.
7. Archivo de automatizacion CI: `.github/workflows/ci.yml`.
8. Pruebas unitarias y funcionales: 26 pruebas en `tests/`.
9. Evidencia de GitHub Actions: runs exitosos y capturas.
10. Release v1.0.0: https://github.com/Styveensoon/TaskManager-DevOps/releases/tag/v1.0.0
11. Evidencia de despliegue: `docs/evidencias-github/08-aplicacion-publicada.png`.
12. URL publica: **https://styveensoon.github.io/TaskManager-DevOps/**
13. Documento de resultados y conclusiones: este archivo.

---

## Preguntas de analisis

1. **Ventajas de GitHub Projects:** centraliza la planificacion en un tablero Kanban, permite visualizar el estado de cada actividad, asignar responsables, priorizar, estimar y dar seguimiento al avance del equipo.
2. **Diferencia entre Git y GitHub:** Git es el sistema distribuido de control de versiones que se ejecuta localmente; GitHub es la plataforma en la nube que aloja repositorios Git y agrega colaboracion, Issues, Projects y Actions.
3. **Importancia de las ramas:** permiten desarrollar funcionalidades de forma aislada sin afectar `main`, facilitan el trabajo paralelo, la revision y evitan integrar codigo inestable.
4. **Funcion de un Pull Request:** proponer cambios de una rama a otra, revisar el codigo, discutir mejoras, ejecutar CI y fusionar solo cuando se cumplen los criterios de calidad.
5. **Problemas que detecta la CI:** errores de sintaxis, pruebas fallidas, regresiones, dependencias incompatibles y conflictos antes de integrar a la rama principal.
6. **Diferencia entre integracion continua y entrega continua:** la CI automatiza la integracion y las pruebas de cada cambio; la entrega continua prepara y valida una version lista para publicarse.
7. **Diferencia entre entrega continua y despliegue continuo:** la entrega continua deja la version lista con aprobacion manual; el despliegue continuo publica automaticamente cada cambio aprobado en produccion.
8. **Importancia de automatizar pruebas:** reducen el tiempo de verificacion, son repetibles, detectan errores temprano y evitan regresiones en cada cambio.
9. **Que sucede si se integra codigo con errores:** la CI falla, el Pull Request queda bloqueado, se notifica al equipo y se corrige con una nueva rama o commit antes de fusionar.
10. **Por que monitorear despues de publicar:** el trabajo no termina en el despliegue; monitorear permite detectar caidas, errores, lentitud y problemas de datos para mantener la disponibilidad y calidad.
11. **Beneficios de DevOps para la empresa:** entregas mas rapidas, mayor calidad, menos errores en produccion, mejor colaboracion, trazabilidad y respuesta agil a cambios.
12. **Como mejorar en una segunda version:** autenticacion, busqueda y filtros, notificaciones, reportes de productividad, pruebas de carga, mayor cobertura y despliegue automatico del backend.

---

## Conclusiones

- La aplicacion TaskManager cumple los seis requerimientos funcionales y esta publicada en una URL accesible.
- La integracion continua con GitHub Actions ejecuta 26 pruebas y bloquea cambios defectuosos; se documento un error real detectado y corregido.
- La entrega continua genera un release y un artefacto descargable; el despliegue publica automaticamente la aplicacion funcional en GitHub Pages.
- Las incidencias de pruebas y de publicacion se corrigieron mediante Issues, ramas y Pull Requests.
- La operacion y el monitoreo dejaron metricas, incidencias y un plan concreto para la version 2.0.0.

**Resultado:** proyecto completo para evaluacion de las 7 fases DevOps.
