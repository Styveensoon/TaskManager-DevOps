## Remedial: Implementación de las fases de DevOps utilizando GitHub

Modalidad: Equipos de 3 integrantes.

Fecha de entrega:

revisión presencial en horario de 14 a 17 hrs.

Herramientas principales: GitHub, Git, GitHub Projects, GitHub Actions y GitHub Issues.

Una pequeña empresa llamada TechSolutions necesita desarrollar un sistema web para administrar las tareas de sus empleados.

Actualmente, la empresa utiliza hojas de cálculo para registrar las actividades, asignar responsables y dar seguimiento a las tareas. Este proceso genera problemas como:

- Pérdida de información.

- Duplicidad de tareas.

- Falta de seguimiento de las actividades.

- Dificultad para identificar tareas pendientes y terminadas.

- Ausencia de pruebas antes de publicar nuevas versiones del sistema.

La empresa ha decidido contratar a un equipo de desarrollo para construir una aplicación web que permita gestionar las tareas de manera centralizada.

Sin embargo, no solamente necesita desarrollar el software, sino también implementar un proceso de trabajo basado en la metodología DevOps, que permita automatizar las actividades de desarrollo, integración, pruebas, entrega y

mantenimiento.

Por lo tanto, asumirán el papel de un equipo de desarrollo y deberán implementar las diferentes fases de DevOps utilizando GitHub como plataforma principal.

25 de noviembre de forma digital y el 26 de noviembre

## 1. Introducción al caso práctico

## 2. Objetivo general

Desarrollar un sistema web de gestión de tareas mediante la aplicación de las fases del ciclo de vida DevOps, utilizando GitHub para administrar el código fuente, planificar actividades, controlar versiones, automatizar pruebas y simular el despliegue de una aplicación.

## 3. Descripción del sistema que deberán desarrollar El sistema se llamará TaskManager.

La aplicación deberá contar con las siguientes funcionalidades:

| Código Funcionalidad | Descripción |
| --- | --- |


| RF01 Registrar tareas Permitir agregar nuevas tareas. |   |
| --- | --- |
| RF02 Consultar tareas Mostrar todas las tareas registradas. |   |
| RF03 Editar tareas | Modificar la información de una tarea. |
| RF04 Eliminar tareas Eliminar tareas existentes. |   |
| RF05 Cambiar estado Cambiar entre pendiente, en proceso y terminada. |   |
| RF06 Asignar prioridadClasificar tareas como alta, media o baja. |   |

## Tecnologías sugeridas:

- Frontend: HTML, CSS y JavaScript.

- Backend: Python con Flask o Node.js.

- Base de datos: SQLite.

- Control de versiones: Git.

- Plataforma colaborativa: GitHub.

- Automatización: GitHub Actions.

- Pruebas: Pytest (si utilizan Python).

## 4. Desarrollo del caso práctico: fases de DevOps

Deberán realizar las siguientes fases. Cada fase contiene una explicación, actividades y evidencias que deberán entregar.

## Fase 1. Planificación (Plan)

Objetivo: Organizar el proyecto, identificar los requerimientos y distribuir las actividades entre los integrantes del equipo.

En esta etapa, el equipo deberá determinar qué se va a desarrollar, cómo se organizará el trabajo y quién será responsable de cada actividad.

- 1. Agregar una descripción: Sistema web para la gestión de tareas.

- 2. Seleccionar la opción Public o Private.

- 3. Activar la opción para agregar un archivo README.

## Actividad 1. Crear un repositorio en GitHub llamado TaskManager- DevOps

## Actividad 2. Crear un tablero de trabajo con GitHub Projects

- 1. Seleccionar una vista tipo Board.


- 2. Crear las siguientes columnas:

- Backlog: actividades pendientes de realizar.

- To Do: actividades que se realizarán.

- In Progress: actividades en desarrollo.

- Review: actividades que están siendo revisadas.

- Done: actividades terminadas.

## Actividad 3. Crear las historias de usuario

Los estudiantes deberán registrar las necesidades del cliente mediante historias de usuario.

## Ejemplo:

Como usuario del sistema, quiero registrar nuevas tareas para organizar mis actividades.

Criterios de aceptación:

- El sistema debe permitir ingresar el nombre de la tarea.

- El sistema debe permitir agregar una descripción.

- El sistema debe permitir seleccionar una prioridad.

- El sistema debe guardar la tarea.

- El sistema debe mostrar un mensaje de confirmación.

## Historia de usuario 1: Registrar tareas

## Historia de usuario 2: Cambiar estado de tareas

Como usuario, quiero cambiar el estado de una tarea para conocer su progreso.

Criterios de aceptación:

- Debe permitir seleccionar pendiente.

- Debe permitir seleccionar en proceso.

- Debe permitir seleccionar terminada.

- El cambio debe reflejarse en el listado de tareas.

## Crear todas las historias de usuario faltantes

## Actividad 4. Crear Issues

Registrar cada actividad mediante Issues.

- Issue #1: Crear la estructura inicial del proyecto.

- Issue #2: Diseñar la interfaz del sistema.

- Issue #3: Implementar el registro de tareas.

- Issue #4: Implementar la edición de tareas.

- Issue #5: Implementar las pruebas unitarias.

## Ejemplos:


## Propiedades que deberá tener cada tarea

Además del nombre y la descripción, cada Issue deberá tener las siguientes propiedades:

| Propiedad Tipo de campo | Valores |
| --- | --- |
| Tarea | Texto / título Nombre de la actividad. |
| Responsable Assignees Integrante asignado. |   |
| Estado Status | Backlog, To Do, In Progress, Review, Done. |
| Prioridad Single select | Crítica, Alta, Media, Baja. |
| Estimación Number | Horas de trabajo estimadas. |
| Fase DevOpsSingle select Plan, Code, Build, Test, Release, Deploy, Operate, Monitor. |   |
| Fecha límite Date Fecha de entrega. |   |

## Evidencias de la fase:

- Repositorio creado.

- Tablero de GitHub Projects.

- Historias de usuario.

- Issues registrados.

- Distribución de responsabilidades.

## Fase 2. Desarrollo (Code)

Desarrollar el código fuente del sistema utilizando Git y GitHub para administrar los cambios realizados por los integrantes del equipo.

En esta fase comenzarán a programar las funcionalidades del sistema.

## Actividad 1. Clonar el repositorio

Primero deberán instalar Git desde: [URL 🔗](https://git-scm.com/?utm_source=chatgpt.com)

Descargar Git . [URL 🔗](https://git-scm.com/?utm_source=chatgpt.com)

Después abrirán una terminal y ejecutarán:

Deberán reemplazar USUARIO por el nombre de su cuenta de GitHub.

bash

cd TaskManager-DevOps

```
bash
git clone https://github.com/USUARIO/TaskManager-DevOps.git
```

## Ingresar al proyecto:


## Actividad 2. Crear la estructura del proyecto

Si utilizan Python con Flask, deberán crear la siguiente estructura:

```
text
TaskManager-DevOps/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│ └── index.html
│
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── app.js
│
└── tests/
└── test_app.py
```

## Actividad 3. Crear ramas de desarrollo

Cada integrante deberá trabajar en una rama independiente.

## Ejemplo:

```
bash
git checkout -b feature/registro-tareas
```

## Otro integrante puede crear:

```
bash
git checkout -b feature/editar-tareas
```

## Y otro:

bash

git checkout -b feature/eliminar-tareas

## Actividad 4. Realizar modificaciones y guardar los cambios

Después de desarrollar una funcionalidad, el estudiante deberá ejecutar:

bash

git add .

## Posteriormente:

```
bash
git commit -m "Agregar funcionalidad de registro de tareas"
```

Finalmente, deberá enviar los cambios a GitHub:

```
bash
git push origin feature/registro-tareas
```


## Actividad 5. Crear un Pull Request

- 1. Ingresar al repositorio en GitHub.

- 2. Seleccionar Pull Requests.

- 3. Seleccionar New Pull Request.

- 4. Elegir la rama que contiene los cambios.

- 5. Compararla con la rama main.

- 6. Describir los cambios realizados.

- 7. Solicitar la revisión de otro integrante.

- 8. Aprobar y combinar los cambios cuando cumplan los criterios establecidos.

- Código fuente del sistema, el sistema debe tener el 90% de funcionalidad solicitada.

- Ramas creadas.

- Commits realizados.

- Pull Requests.

- Historial de modificaciones.

## Evidencias de la fase:

## Fase 3. Integración continua (Continuous Integration - CI)

Automatizar la integración del código y ejecutar pruebas cada vez que los desarrolladores envíen cambios al repositorio.

En esta etapa se utilizará GitHub Actions.

La integración continua permite detectar errores antes de incorporar los cambios al proyecto principal.

## Actividad 1. Crear pruebas unitarias

Deberán desarrollar pruebas para verificar que las funcionalidades del sistema trabajen correctamente.

Por ejemplo, si utilizan Python, pueden crear el archivo:

```
tests/test_app.py
```

## Ejemplo de prueba:

```
python
def test_registro_tarea():
tarea = {
"nombre": "Realizar actividad DevOps",
"estado": "Pendiente"
}
assert tarea["nombre"] == "Realizar actividad DevOps"
assert tarea["estado"] == "Pendiente"
```


Esta prueba verifica que una tarea tenga el nombre y estado esperados.

Posteriormente, deberán desarrollar pruebas que interactúen con las funciones reales de la aplicación.

## Actividad 2. Crear el archivo de automatización

Dentro del repositorio deberán crear las siguientes carpetas y archivo:

```
text
.github/
workflows/
ci.yml
```

El archivo ci.yml contendrá las instrucciones para ejecutar las pruebas automáticamente.

## Ejemplo:

```
yaml
name: Integracion Continua
on:
push:
branches: [main]
pull_request:
branches: [main]
jobs:
pruebas:
runs-on: ubuntu-latest
steps:
- name: Descargar codigo
uses: actions/checkout@v4
- name: Configurar Python
uses: actions/setup-python@v5
with:
python-version: '3.12'
- name: Instalar dependencias
run: |
pip install -r requirements.txt
- name: Ejecutar pruebas
run: |
pytest
```

## Actividad 3. Ejecutar el flujo de trabajo

Una vez guardado el archivo:

- 1. Realizar un commit.

- 2. Enviar los cambios a GitHub.

- 3. Ingresar a la pestaña Actions.

- 4. Identificar el flujo de trabajo creado.

- 5. Revisar si las pruebas se ejecutaron correctamente.


- 6. Consultar los resultados.

## Pruebas aprobadas

Error

El código cumple las pruebas automatizadas.

## Pruebas fallidas

- Archivo ci.yml.

- Pruebas unitarias.

- Ejecución de GitHub Actions.

- Capturas de ejecuciones exitosas.

- Registro de errores detectados y corregidos.

Verificar que el sistema cumpla con los requerimientos establecidos y que las funcionalidades trabajen correctamente.

El equipo debe analizar y corregir los errores.

## Evidencias de la fase:

## Fase 4. Pruebas (Test)

## Actividad 1. Diseñar casos de prueba

Los estudiantes deberán elaborar una matriz de pruebas como la siguiente:

| ID | Prueba | Resultado esperado |
| --- | --- | --- |
|   | CP01Registrar una tarea | La tarea se guarda correctamente. |
| CP02Registrar una tarea sin nombreEl sistema muestra una validación. |   |   |
| CP03Consultar tareas |   | Se muestra el listado. |
| CP04Editar una tarea |   | Se actualiza la información. |
|   | CP05Eliminar una tarea | La tarea desaparece del listado. |
| CP06Cambiar estado |   | Se actualiza el estado. |
| CP07Seleccionar prioridad |   | Se guarda la prioridad elegida. |

## Actividad 2. Realizar pruebas funcionales

Deberán ejecutar manualmente cada caso de prueba.

Por ejemplo:

- 1. Abrir el sistema.

- 2. Seleccionar la opción Nueva tarea. 3. Escribir el nombre: Elaborar documentación.

- 4. Agregar una descripción.

## Prueba CP01: Registrar una tarea


- 5. Seleccionar prioridad alta.

- 6. Guardar la tarea.

- 7. Verificar que aparezca en el listado.

Resultado esperado: La tarea debe registrarse correctamente.

## Actividad 3. Reportar errores mediante GitHub Issues

Si encuentran algún error, deberán crear un Issue.

Título: Error al guardar tareas sin descripción.

- Funcionalidad afectada: Registro de tareas.

- Pasos para reproducir: Intentar guardar una tarea sin descripción.

- Resultado obtenido: El sistema genera un error inesperado.

- Resultado esperado: El sistema debe validar el campo.

- Prioridad: Alta.

Deberá corregir el error mediante una rama y un Pull Request.

- Matriz de casos de prueba.

- Resultados de las pruebas.

- Issues de errores encontrados.

- Evidencias de corrección.

- Nueva ejecución exitosa de GitHub Actions.

Preparar una versión estable del sistema para que pueda ser entregada y desplegada.

Deberán comprobar que el proyecto esté listo para publicarse.

## Ejemplo:

## Descripción:

## Evidencias de la fase:

## Fase 5. Entrega continua (Continuous Delivery)

## Actividad 1. Revisar la versión estable

Antes de entregar el proyecto deberán verificar:

- Que todas las funcionalidades estén implementadas.

- Que las pruebas estén aprobadas.

- Que no existan errores críticos conocidos.

- Que el código esté integrado en main.

- Que exista documentación del sistema.

## Actividad 2. Crear una versión del proyecto

En GitHub deberán:

- 1. Ingresar a Releases.


- 2. Seleccionar Create a new release.

- 3. Crear una etiqueta denominada v1.0.0.

- 4. Escribir como título: Primera versión estable de TaskManager.

- 5. Describir las funcionalidades incorporadas.

- 6. Publicar el Release.

## Actividad 3. Preparar la automatización de entrega

Los estudiantes deberán configurar GitHub Actions para generar un artefacto con el código del proyecto.

Por ejemplo, pueden agregar otro workflow que se ejecute cuando se publique una versión:

```
yaml
name: Entrega Continua
on:
release:
types: [published]
jobs:
entrega:
runs-on: ubuntu-latest
steps:
- name: Descargar codigo
uses: actions/checkout@v4
- name: Preparar artefacto
uses: actions/upload-artifact@v4
with:
name: TaskManager-v1
path: |
app.py
requirements.txt
templates/
static/
```

Este ejemplo prepara un paquete descargable del proyecto; no publica automáticamente la aplicación en un servidor.

## Evidencias de la fase:

- Versión estable v1.0.0.

- Release publicado.

- Workflow de entrega.

- Artefacto generado.

- Notas de versión.

## Fase 6. Despliegue continuo (Continuous Deployment)


Publicar la aplicación para que pueda ser utilizada por los usuarios finales.

Deberán llevar el sistema desde el entorno de desarrollo hasta un entorno de publicación.

## Actividad 1. Seleccionar un servicio de despliegue

Pueden utilizar alguna de estas plataformas: [URL 🔗](https://render.com/?utm_source=chatgpt.com)

- [Render .](https://render.com/?utm_source=chatgpt.com)

- [Railway .](https://railway.com/?utm_source=chatgpt.com)

- [Fly.io .](https://fly.io/?utm_source=chatgpt.com)

La plataforma seleccionada deberá ser compatible con la tecnología que utilizaron.

## Actividad 2. Configurar el despliegue

Si utilizan Flask:

- 1. Crear una cuenta en el servicio seleccionado.

- 2. Conectar la cuenta de GitHub.

- 3. Seleccionar el repositorio TaskManager-DevOps.

- 4. Configurar el comando de instalación.

- 5. Configurar el comando de inicio de la aplicación.

- 6. Configurar las variables de entorno necesarias.

- 7. Seleccionar Deploy.

- 8. Esperar a que finalice el proceso.

Ejemplo de comandos para una aplicación Flask:

```
bash
# Instalación
pip install -r requirements.txt
# Inicio
gunicorn app:app
```

Para utilizar este ejemplo deberán agregar gunicorn a requirements.txt y configurar correctamente la aplicación Flask.

## Actividad 3. Verificar la aplicación publicada

Una vez desplegado el sistema, deberán comprobar:

- Que la URL de la aplicación sea accesible.

- Que la página principal cargue correctamente.

- Que se puedan registrar tareas.

- Que las tareas se puedan editar.

- Que se puedan eliminar.

- Que los estados se actualicen correctamente.

- Plataforma de despliegue configurada.

- URL pública del sistema.

## Evidencias de la fase:


- Capturas de la aplicación funcionando.

- Evidencia del proceso de despliegue.

## Fase 7. Operación y monitoreo (Operate & Monitor)

Supervisar el funcionamiento del sistema después de su publicación e identificar posibles errores o problemas de rendimiento.

En DevOps, el trabajo no termina cuando la aplicación se publica. Es necesario verificar que continúe funcionando correctamente.

## Actividad 1. Monitorear el funcionamiento

Deberán verificar:

- Disponibilidad de la aplicación.

- Tiempo de respuesta.

- Errores que presente el sistema.

- Correcto almacenamiento de la información.

- Funcionamiento de las funcionalidades principales.

## Actividad 2. Crear un registro de incidencias

Deberán utilizar GitHub Issues para documentar los problemas detectados.

Título: La aplicación no permite guardar nuevas tareas.

Descripción:

- Fecha de detección.

- Funcionalidad afectada.

- Descripción del problema.

- Evidencia del error.

- Responsable de corregirlo.

- Solución aplicada.

## Ejemplo:

## Actividad 3. Proponer mejoras

Ejemplos:

- Implementar autenticación de usuarios.

- Agregar filtros de búsqueda.

- Incorporar notificaciones.

- Agregar reportes de productividad.

- Mejorar el rendimiento de la aplicación.

- Registro de monitoreo.

- Incidencias documentadas.

El equipo deberá identificar al menos tres mejoras para una futura versión.

## Evidencias de la fase:


- Propuestas de mejora.

- Planeación de una nueva versión.

El siguiente esquema muestra cómo se relacionan las fases con las herramientas de GitHub:

| Fase DevOps | Herramienta | Producto o resultado |
| --- | --- | --- |
| Planificación | GitHub Projects e Issues | Actividades organizadas. |
| Desarrollo | Git y GitHub | Código fuente y versiones. |
| Integración continua GitHub Actions |   | Código integrado |
|   |   | automáticamente. |
| Pruebas | GitHub Actions y Pytest | Pruebas ejecutadas. |
| Entrega continua | GitHub Releases y Actions | Versión estable preparada. |
| Despliegue |   | GitHub Actions y servicio cloud Aplicación publicada. |
| Operación y | Issues y herramientas de | Incidencias y mejoras. |
| monitoreo | monitoreo |   |

## 6. Organización del equipo de trabajo

Se recomienda integrar equipos de cuatro estudiantes.

| Rol | Responsabilidades |
| --- | --- |
| Product Owner | Identificar requerimientos y organizar prioridades. |
| Desarrollador 1 | Programar las funcionalidades principales. |
| Desarrollador 2 | Desarrollar la interfaz y funcionalidades adicionales. |
| Ingeniero DevOps / QAConfigurar GitHub Actions, pruebas y despliegue. |   |

Todos los integrantes deberán participar en las revisiones de código y conocer las diferentes fases de DevOps.

## 7. Entregables del proyecto

Al finalizar el caso práctico, cada equipo deberá entregar:

- 1. URL del repositorio de GitHub.

- 2. Tablero de GitHub Projects.

- 3. Historias de usuario.


- 4. Issues creados y atendidos.

- 5. Código fuente completo.

- 6. Ramas y Pull Requests.

- 7. Archivo de automatización CI.

- 8. Pruebas unitarias y funcionales.

- 9. Evidencia de ejecución de GitHub Actions.

- 10.Release v1.0.0.

- 11.Evidencia de despliegue.

- 12.URL pública de la aplicación.

- 13.Documento de resultados y conclusiones.

## 8. Rúbrica de evaluación

La evaluación estará basada en el cumplimiento de las fases de DevOps y en las evidencias generadas durante el desarrollo.

| Criterio | Ponderación |
| --- | --- |
| Planificación y organización del proyecto10% |   |
| Desarrollo y control de versiones | 20% |
| Integración continua con GitHub Actions 15% |   |
| Diseño y ejecución de pruebas | 15% |
| Entrega continua y Releases | 10% |
| Despliegue de la aplicación | 15% |
| Operación y monitoreo | 10% |
| Documentación y presentación | 5% |
| Total | 100% |

## 9. Preguntas de análisis

Una vez terminado el proyecto, cada equipo deberá responder las siguientes preguntas:

- 1. ¿Qué ventajas ofrece utilizar GitHub Projects para organizar un proyecto de software?

- 2. ¿Cuál es la diferencia entre Git y GitHub?

- 3. ¿Por qué es importante utilizar ramas durante el desarrollo?

- 4. ¿Qué función cumple un Pull Request?

- 5. ¿Qué problemas permite detectar la integración continua?

- 6. ¿Cuál es la diferencia entre integración continua y entrega continua?


- 7. ¿Qué diferencia existe entre entrega continua y despliegue continuo?

- 8. ¿Por qué es importante automatizar las pruebas?

- 9. ¿Qué sucede si se integra código que contiene errores?

- 10.¿Por qué DevOps requiere monitorear una aplicación después de publicarla?

- 11.¿Qué beneficios obtiene una empresa al implementar DevOps?

- 12.¿Cómo podrían mejorar el proceso de desarrollo en una segunda versión?
