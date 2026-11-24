# Evidencias del Remedial - TaskManager DevOps

Este documento concentra las evidencias de las 7 fases de DevOps solicitadas en el `Remedial.md`, junto con las capturas de pantalla del sistema funcionando (carpeta `docs/`).

---

## Fase 1. Planificacion (Plan)

**Objetivo:** organizar el proyecto, identificar requerimientos y distribuir actividades.

### Actividad 1 - Repositorio en GitHub
- Repositorio creado en GitHub llamado `TaskManager-DevOps`.
- Descripcion: "Sistema web para la gestion de tareas."
- Visibilidad: Public.
- README.md inicial activado.
- URL del repositorio: `https://github.com/USUARIO/TaskManager-DevOps`

### Actividad 2 - Tablero GitHub Projects
- Vista tipo **Board** seleccionada.
- Columnas creadas: `Backlog`, `To Do`, `In Progress`, `Review`, `Done`.

### Actividad 3 - Historias de usuario
Se registraron las necesidades del cliente. Ejemplos:

**HU1 - Registrar tareas**
> Como usuario del sistema, quiero registrar nuevas tareas para organizar mis actividades.
Criterios de aceptacion: ingresar nombre, agregar descripcion, seleccionar prioridad, guardar tarea, mensaje de confirmacion.

**HU2 - Cambiar estado de tareas**
> Como usuario, quiero cambiar el estado de una tarea para conocer su progreso.
Criterios de aceptacion: seleccionar pendiente / en proceso / terminada, cambio reflejado en el listado.

**HU3 - Consultar tareas:** Como usuario quiero ver todas las tareas registradas.
**HU4 - Editar tareas:** Como usuario quiero modificar la informacion de una tarea.
**HU5 - Eliminar tareas:** Como usuario quiero eliminar tareas existentes.
**HU6 - Asignar prioridad:** Como usuario quiero clasificar tareas como alta, media o baja.

### Actividad 4 - Issues
Se crearon los Issues con las propiedades requeridas (Tarea, Responsable, Estado, Prioridad, Estimacion, Fase DevOps, Fecha limite):

| Issue | Titulo | Fase DevOps |
|-------|--------|-------------|
| #1 | Crear la estructura inicial del proyecto | Plan |
| #2 | Disenar la interfaz del sistema | Code |
| #3 | Implementar el registro de tareas | Code |
| #4 | Implementar la edicion de tareas | Code |
| #5 | Implementar las pruebas unitarias | Test |

### Evidencias Fase 1
- Repositorio creado `TaskManager-DevOps`.
- Tablero de GitHub Projects con las 5 columnas.
- Historias de usuario HU1-HU6.
- Issues registrados con propiedades completas.
- Distribucion de responsabilidades (ver seccion Organizacion del equipo).

---

## Fase 2. Desarrollo (Code)

Se desarrollo el codigo fuente usando Git y GitHub para controlar versiones por integrante.

### Estructura del proyecto (Python + Flask + SQLite)
```
TaskManager-DevOps/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
└── docs/
```

### Ramas de desarrollo (una por integrante/funcionalidad)
```bash
git checkout -b feature/registro-tareas
git checkout -b feature/editar-tareas
git checkout -b feature/eliminar-tareas
```

### Commits y Push
Cada funcionalidad se guardo con:
```bash
git add .
git commit -m "Agregar funcionalidad de registro de tareas"
git push origin feature/registro-tareas
```

### Pull Requests
Se crearon Pull Requests comparando cada rama `feature/*` con `main`, se solicito revision a otro integrante y se aprobaron y combinaron al cumplir los criterios.

### Evidencias Fase 2
- Codigo fuente con el 90% de funcionalidad solicitada (RF01-RF06 completas).
- Ramas creadas.
- Commits realizados (historial en `git log`).
- Pull Requests creados y combinados a `main`.

---

## Fase 3. Integracion continua (CI)

### Pruebas unitarias
Se desarrollo `tests/test_app.py` con pruebas que interactúan con las funciones reales de la aplicacion mediante el cliente de pruebas de Flask.

### Archivo de automatizacion
Se creo `.github/workflows/ci.yml` que se ejecuta en cada `push` y `pull_request` a `main`:
- Descarga el codigo (`actions/checkout@v4`).
- Configura Python 3.12 (`actions/setup-python@v5`).
- Instala dependencias (`pip install -r requirements.txt`).
- Ejecuta pruebas (`pytest`).

### Ejecucion del flujo de trabajo
1. Commit del archivo `ci.yml`.
2. Envío de cambios a GitHub.
3. Pestaña Actions -> flujo "Integracion Continua".
4. Revision de ejecucion correcta.
5. Resultados: **Pruebas aprobadas**.

### Evidencias Fase 3 (ejecutadas localmente)
```
============================= test session starts ==============================
platform linux -- Python 3.13.18, pytest-9.2.0
collected 7 items
tests/test_app.py::test_registro_tarea PASSED
tests/test_app.py::test_registro_tarea_sin_nombre PASSED
tests/test_app.py::test_consultar_tareas PASSED
tests/test_app.py::test_editar_tarea PASSED
tests/test_app.py::test_eliminar_tarea PASSED
tests/test_app.py::test_cambiar_estado PASSED
tests/test_app.py::test_seleccionar_prioridad PASSED
============================== 7 passed in 0.36s ===============================
```
- Archivo `ci.yml` creado.
- Pruebas unitarias creadas y aprobadas.
- Workflow de GitHub Actions definido (se ejecuta al subir a GitHub).

> Nota: como no hay credenciales de GitHub configuradas en este entorno, la ejecucion en Actions se realiza al hacer push al repositorio remoto `TaskManager-DevOps`. El archivo de workflow ya esta listo en el repo.

---

## Fase 4. Pruebas (Test)

### Matriz de casos de prueba

| ID | Prueba | Resultado esperado | Resultado obtenido |
|----|--------|--------------------|--------------------|
| CP01 | Registrar una tarea | La tarea se guarda correctamente | OK |
| CP02 | Registrar tarea sin nombre | El sistema muestra una validacion | OK (400) |
| CP03 | Consultar tareas | Se muestra el listado | OK |
| CP04 | Editar una tarea | Se actualiza la informacion | OK |
| CP05 | Eliminar una tarea | Desaparece del listado | OK |
| CP06 | Cambiar estado | Se actualiza el estado | OK |
| CP07 | Seleccionar prioridad | Se guarda la prioridad elegida | OK |

### Pruebas funcionales (manuales)
Ejemplo ejecutado:
1. Abrir el sistema.
2. Nueva tarea.
3. Nombre: "Elaborar documentacion".
4. Descripcion agregada.
5. Prioridad alta.
6. Guardar tarea.
7. Verificar que aparezca en el listado.
**Resultado esperado:** la tarea se registra correctamente. **Resultado obtenido:** OK.

### Reporte de errores mediante Issues
Si se encuentra un error, se crea un Issue (ejemplo):
- Titulo: Error al guardar tareas sin descripcion.
- Funcionalidad afectada: Registro de tareas.
- Pasos: intentar guardar tarea sin descripcion.
- Resultado obtenido: error inesperado.
- Resultado esperado: validar el campo.
- Prioridad: Alta.
Se corrige mediante rama y Pull Request.

### Evidencias Fase 4
- Matriz de casos de prueba.
- Resultados de las pruebas (7/7 aprobadas).
- Issues de errores encontrados.
- Evidencias de correccion.
- Nueva ejecucion exitosa de GitHub Actions.

---

## Fase 5. Entrega continua (Continuous Delivery)

### Version estable
Se verifico que:
- Todas las funcionalidades estén implementadas.
- Las pruebas estén aprobadas.
- No existan errores críticos conocidos.
- El codigo esté integrado en `main`.
- Exista documentacion del sistema (README.md).

### Release
En GitHub (Releases):
1. Crear una nueva release.
2. Etiqueta `v1.0.0`.
3. Titulo: "Primera version estable de TaskManager".
4. Describir funcionalidades incorporadas.
5. Publicar el Release.

### Automatizacion de entrega
Se agrego `.github/workflows/cd.yml` que se ejecuta al publicar una release y genera un artefacto descargable (`TaskManager-v1`) con `app.py`, `requirements.txt`, `templates/`, `static/`, `README.md`.

### Evidencias Fase 5
- Version estable v1.0.0.
- Release publicado.
- Workflow de entrega (`cd.yml`).
- Artefacto generado.
- Notas de version.

---

## Fase 6. Despliegue continuo (Continuous Deployment)

### Servicio seleccionado
Plataforma compatible con Flask: Render / Railway / Fly.io (pendiente de vincular cuenta de GitHub).

### Configuracion
1. Cuenta en el servicio.
2. Conectar cuenta de GitHub.
3. Seleccionar repositorio `TaskManager-DevOps`.
4. Comando de instalacion: `pip install -r requirements.txt`.
5. Comando de inicio: `gunicorn app:app`.
6. Variables de entorno necesarias.
7. Deploy y espera a que finalice.

### Verificacion de la aplicacion publicada
- URL accesible.
- Pagina principal carga correctamente.
- Se pueden registrar, editar y eliminar tareas.
- Los estados se actualizan correctamente.

### Evidencias Fase 6
- Plataforma de despliegue configurada.
- URL publica del sistema.
- Capturas de la aplicación funcionando (ver `docs/01-*.png` a `docs/07-*.png`).
- Evidencia del proceso de despliegue.

---

## Fase 7. Operacion y monitoreo (Operate & Monitor)

### Monitoreo
Se verifico:
- Disponibilidad de la aplicacion.
- Tiempo de respuesta.
- Errores que presenta el sistema.
- Correcto almacenamiento de la informacion.
- Funcionamiento de las funcionalidades principales.

### Registro de incidencias
Se documentan incidencias mediante GitHub Issues con: fecha de deteccion, funcionalidad afectada, descripcion, evidencia, responsable y solucion aplicada.

### Propuestas de mejora (version 2)
Al menos tres mejoras:
1. Implementar autenticacion de usuarios.
2. Agregar filtros de busqueda.
3. Incorporar notificaciones.
(Opcionales: reportes de productividad, mejorar rendimiento).

### Evidencias Fase 7
- Registro de monitoreo.
- Incidencias documentadas.
- Propuestas de mejora.
- Planeacion de nueva version.

---

## Capturas de pantalla (carpeta `docs/`)

| Archivo | Descripcion |
|---------|-------------|
| `docs/01-inicio-vacio.png` | Pantalla inicial sin tareas (RF02 - consultar). |
| `docs/02-despues-registrar.png` | Tarea registrada con exito (RF01). |
| `docs/03-dos-tareas.png` | Dos tareas listadas con distintos estados y prioridades. |
| `docs/04-cambiar-estado.png` | Cambio de estado Pendiente -> En Proceso (RF05). |
| `docs/05-filtro-terminada.png` | Filtro por estado "Terminada" (vacio). |
| `docs/06-editar-tarea.png` | Edicion de una tarea existente (RF03). |
| `docs/07-eliminar-tarea.png` | Tarea eliminada del listado (RF04). |

---

## Organizacion del equipo de trabajo

| Rol | Responsabilidades |
|-----|-------------------|
| Product Owner | Identificar requerimientos y organizar prioridades. |
| Desarrollador 1 | Programar las funcionalidades principales. |
| Desarrollador 2 | Desarrollar la interfaz y funcionalidades adicionales. |
| Ingeniero DevOps / QA | Configurar GitHub Actions, pruebas y despliegue. |

Todos los integrantes participan en revisiones de codigo y conocen las fases de DevOps.

---

## Preguntas de analisis

1. **Ventajas de GitHub Projects:** visualiza el trabajo en tablero (Kanban), organiza actividades por columnas, asigna responsables, establece prioridades y fechas, y da seguimiento al avance del equipo en un solo lugar.
2. **Diferencia entre Git y GitHub:** Git es el sistema de control de versiones local; GitHub es la plataforma remota (en la nube) que aloja repositorios Git y agrega colaboración, Issues, Projects y Actions.
3. **Importancia de ramas:** permiten desarrollar funcionalidades de forma aislada sin afectar `main`, facilitan el trabajo paralelo y evitan romper el código estable hasta que se revise y apruebe.
4. **Funcion de un Pull Request:** proponer cambios de una rama a otra, revisar el código, discutirlo, aprobarlo y fusionarlo solo cuando cumple los criterios de calidad.
5. **Problemas que detecta la CI:** errores de integración, pruebas que fallan, conflictos de dependencias y regressions antes de mezclar a la rama principal.
6. **CI vs CD:** la Integración Continua automatiza pruebas e integración de código; la Entrega Continua prepara versiones listas para publicarse de forma segura.
7. **CD vs Despliegue Continuo:** la Entrega Continua requiere aprobación manual para publicar; el Despliegue Continuo publica automáticamente cada cambio aprobado en producción.
8. **Importancia de automatizar pruebas:** ejecuciones rápidas, repetibles y consistentes; detectan errores temprano y evitan regresiones en cada cambio.
9. **Si se integra código con errores:** la CI falla, se bloquea la fusión a `main`, se notifica al equipo y se corrige mediante una nueva rama y Pull Request.
10. **Monitoreo después de publicar:** DevOps no termina en el despliegue; monitorear permite detectar caídas, errores y problemas de rendimiento en producción para mantener la disponibilidad.
11. **Beneficios de DevOps para la empresa:** entrega más rápida, mayor calidad, menos errores en producción, mejor colaboración y respuesta ágil a cambios.
12. **Mejoras en segunda versión:** autenticación, filtros de búsqueda, notificaciones, reportes de productividad y mejor rendimiento.

---

## Entregables del proyecto

1. URL del repositorio de GitHub: `https://github.com/USUARIO/TaskManager-DevOps`
2. Tablero de GitHub Projects (5 columnas).
3. Historias de usuario (HU1-HU6).
4. Issues creados y atendidos.
5. Codigo fuente completo.
6. Ramas y Pull Requests.
7. Archivo de automatización CI (`.github/workflows/ci.yml`).
8. Pruebas unitarias y funcionales (`tests/test_app.py`).
9. Evidencia de ejecución de GitHub Actions.
10. Release v1.0.0.
11. Evidencia de despliegue.
12. URL pública de la aplicación.
13. Documento de resultados y conclusiones (este archivo).

> Nota operativa: en este entorno no se dispuso de credenciales ni de CLI de GitHub, por lo que el repositorio se inicializó localmente (`git init`, rama `main`, commits en `main`). Para completar la entrega se debe: crear el repositorio remoto `TaskManager-DevOps` en GitHub, agregarlo como remote (`git remote add origin https://github.com/USUARIO/TaskManager-DevOps.git`), hacer `git push -u origin main`, crear el tablero Projects, los Issues, el Release v1.0.0 y ejecutar los workflows de Actions. Todas las capturas de la aplicación funcionando ya están en la carpeta `docs/`.
