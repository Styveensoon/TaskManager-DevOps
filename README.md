# TaskManager - DevOps

Sistema web para la gestion de tareas de empleados, desarrollado como parte del remedial de fases de DevOps utilizando GitHub.

## Tecnologias
- Frontend: HTML, CSS y JavaScript
- Backend: Python con Flask
- Base de datos: SQLite
- Control de versiones: Git / GitHub
- Automatizacion: GitHub Actions (CI/CD)
- Pruebas: Pytest

## Estructura del proyecto
```
TaskManager-DevOps/
├── app.py
├── requirements.txt
├── README.md
├── tasks.db                 (generada al ejecutar)
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
└── docs/                    (evidencias y capturas de pantalla)
```

## Funcionalidades (Requerimientos funcionales)
- RF01: Registrar tareas
- RF02: Consultar tareas
- RF03: Editar tareas
- RF04: Eliminar tareas
- RF05: Cambiar estado (Pendiente, En Proceso, Terminada)
- RF06: Asignar prioridad (Alta, Media, Baja)

## Instalacion y ejecucion local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/USUARIO/TaskManager-DevOps.git
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

## Ejecutar pruebas
```bash
pytest
```

## Despliegue (ejemplo Flask en Render/Railway)
- Instalacion: `pip install -r requirements.txt`
- Inicio: `gunicorn app:app`
- Agregar `gunicorn` a `requirements.txt` (ya incluido).

## Fases DevOps implementadas
1. Planificacion: GitHub Projects (tablero) e Issues
2. Desarrollo: ramas feature/*, commits y Pull Requests
3. Integracion continua: .github/workflows/ci.yml + pytest
4. Pruebas: matriz de casos de prueba y pruebas unitarias
5. Entrega continua: Release v1.0.0 + .github/workflows/cd.yml
6. Despliegue: servicio cloud (Render / Railway / Fly.io)
7. Operacion y monitoreo: Issues de incidencias y propuestas de mejora
