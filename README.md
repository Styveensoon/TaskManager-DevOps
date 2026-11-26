# TaskManager - DevOps

Sistema web para la gestion de tareas de empleados, desarrollado como parte del remedial de fases de DevOps utilizando GitHub como plataforma principal.

[![Integracion Continua](https://github.com/Styveensoon/TaskManager-DevOps/actions/workflows/ci.yml/badge.svg)](https://github.com/Styveensoon/TaskManager-DevOps/actions/workflows/ci.yml)
[![Desplegar en GitHub Pages](https://github.com/Styveensoon/TaskManager-DevOps/actions/workflows/pages.yml/badge.svg)](https://github.com/Styveensoon/TaskManager-DevOps/actions/workflows/pages.yml)

## Aplicacion publicada

- **URL publica (version funcional):** https://styveensoon.github.io/TaskManager-DevOps/
- **Repositorio:** https://github.com/Styveensoon/TaskManager-DevOps
- **GitHub Projects:** https://github.com/users/Styveensoon/projects/1
- **Release v1.0.0:** https://github.com/Styveensoon/TaskManager-DevOps/releases/tag/v1.0.0
- **GitHub Actions:** https://github.com/Styveensoon/TaskManager-DevOps/actions
- **Evidencias completas:** [docs/EVIDENCIAS_REMEDIAL.md](docs/EVIDENCIAS_REMEDIAL.md)
- **Monitoreo:** [docs/MONITOREO.md](docs/MONITOREO.md)

> La pagina publicada es la **aplicacion funcional** (registrar, consultar, editar, eliminar, cambiar estado y prioridad). El despliegue se realiza con `.github/workflows/pages.yml` sobre la carpeta `docs/`, no con el README.

## Tecnologias
- Frontend: HTML, CSS y JavaScript
- Backend: Python con Flask
- Base de datos: SQLite
- Control de versiones: Git / GitHub
- Automatizacion: GitHub Actions (CI/CD)
- Pruebas: Pytest (13 pruebas automatizadas)
- Despliegue: GitHub Pages (version estatica funcional)

## Funcionalidades (Requerimientos funcionales)
| Codigo | Funcionalidad | Estado |
|--------|---------------|--------|
| RF01 | Registrar tareas | Implementado |
| RF02 | Consultar tareas | Implementado |
| RF03 | Editar tareas | Implementado |
| RF04 | Eliminar tareas | Implementado |
| RF05 | Cambiar estado (Pendiente, En Proceso, Terminada) | Implementado |
| RF06 | Asignar prioridad (Alta, Media, Baja) | Implementado |

## Estructura del proyecto
```
TaskManager-DevOps/
├── app.py                    # API Flask + SQLite (backend)
├── requirements.txt
├── README.md
├── tasks.db                  # generada al ejecutar (no se versiona)
├── templates/
│   └── index.html
├── static/
│   ├── css/style.css
│   └── js/app.js
├── docs/                     # sitio publicado + evidencias + capturas
│   ├── index.html            # aplicacion estatica publicada en GitHub Pages
│   ├── css/style.css
│   ├── js/app.js
│   ├── EVIDENCIAS_REMEDIAL.md
│   └── MONITOREO.md
├── tests/
│   ├── conftest.py
│   └── test_app.py           # 13 pruebas automatizadas
└── .github/
    └── workflows/
        ├── ci.yml            # Integracion continua (pytest)
        ├── cd.yml            # Entrega continua (release -> artefacto)
        └── pages.yml         # Despliegue continuo en GitHub Pages
```

## Instalacion y ejecucion local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Styveensoon/TaskManager-DevOps.git
   cd TaskManager-DevOps
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicacion:
   ```bash
   python app.py
   ```

5. Abrir en el navegador: http://localhost:5000

Tambien se puede cambiar la base de datos con la variable `TASKMANAGER_DB`:
```bash
TASKMANAGER_DB=/tmp/taskmanager.db python app.py
```

## API REST
| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| GET | `/` | Interfaz web |
| GET | `/api/tareas` | Listar tareas |
| POST | `/api/tareas` | Registrar tarea |
| GET | `/api/tareas/<id>` | Consultar una tarea |
| PUT | `/api/tareas/<id>` | Editar tarea |
| PATCH | `/api/tareas/<id>/estado` | Cambiar estado |
| DELETE | `/api/tareas/<id>` | Eliminar tarea |
| GET | `/health` y `/api/health` | Estado, version y total de tareas (monitoreo) |

## Ejecutar pruebas
```bash
pytest -v
```
Las pruebas usan una base SQLite temporal (`tmp_path`) y no modifican `tasks.db`.

## Despliegue
- **GitHub Pages (publicado):** workflow `pages.yml` publica `docs/` en https://styveensoon.github.io/TaskManager-DevOps/.
- **Backend Flask (opcional):** instalacion `pip install -r requirements.txt`, inicio `gunicorn app:app`; compatible con Render, Railway o Fly.io.

## Fases DevOps implementadas
1. **Planificacion:** GitHub Projects (tablero), historias de usuario HU1-HU6 e Issues con propiedades.
2. **Desarrollo:** ramas `feature/*`, `fix/*`, `ci/*`, commits y Pull Requests revisados y fusionados.
3. **Integracion continua:** `.github/workflows/ci.yml` ejecuta pytest en cada push y Pull Request.
4. **Pruebas:** matriz CP01-CP08, pruebas unitarias/funcionales y correccion de errores mediante Issues.
5. **Entrega continua:** Release `v1.0.0` + `.github/workflows/cd.yml` que genera el artefacto `TaskManager-v1`.
6. **Despliegue:** `.github/workflows/pages.yml` publica la aplicacion funcional en GitHub Pages.
7. **Operacion y monitoreo:** endpoint `/health`, registro de monitoreo, incidencias y mejoras planificadas para v2.0.0.

## Equipo
| Rol | Responsabilidad |
|-----|-----------------|
| Product Owner | Requerimientos y prioridades |
| Desarrollador 1 | Funcionalidades principales y backend |
| Desarrollador 2 | Interfaz, estilos y funcionalidades adicionales |
| Ingeniero DevOps / QA | CI/CD, pruebas, despliegue y monitoreo |
