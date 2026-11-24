import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    # Usar una base de datos temporal para las pruebas
    import os

    app.config["DB_PATH"] = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "test_tasks.db"
    )

    with app.test_client() as client:
        yield client

    # Limpiar base de datos de prueba al finalizar
    try:
        os.remove(app.config["DB_PATH"])
    except FileNotFoundError:
        pass


def test_registro_tarea(client):
    """CP01: Registrar una tarea con nombre, descripcion y prioridad."""
    respuesta = client.post(
        "/api/tareas",
        json={
            "nombre": "Elaborar documentacion",
            "descripcion": "Redactar el manual de usuario",
            "prioridad": "Alta",
            "estado": "Pendiente",
        },
    )
    assert respuesta.status_code == 201
    datos = respuesta.get_json()
    assert datos["nombre"] == "Elaborar documentacion"
    assert datos["prioridad"] == "Alta"
    assert datos["estado"] == "Pendiente"
    assert datos["id"] is not None


def test_registro_tarea_sin_nombre(client):
    """CP02: Registrar una tarea sin nombre debe fallar con validacion."""
    respuesta = client.post(
        "/api/tareas",
        json={"nombre": "", "descripcion": "Sin nombre", "prioridad": "Media"},
    )
    assert respuesta.status_code == 400


def test_consultar_tareas(client):
    """CP03: Consultar tareas registradas se muestra el listado."""
    client.post(
        "/api/tareas",
        json={"nombre": "Tarea A", "descripcion": "Desc A", "prioridad": "Baja"},
    )
    respuesta = client.get("/api/tareas")
    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert any(t["nombre"] == "Tarea A" for t in datos)


def test_editar_tarea(client):
    """CP04: Editar una tarea actualiza la informacion."""
    crear = client.post(
        "/api/tareas",
        json={"nombre": "Original", "descripcion": "Desc", "prioridad": "Media"},
    )
    tarea_id = crear.get_json()["id"]

    respuesta = client.put(
        f"/api/tareas/{tarea_id}",
        json={"nombre": "Modificada", "prioridad": "Alta"},
    )
    assert respuesta.status_code == 200
    datos = respuesta.get_json()
    assert datos["nombre"] == "Modificada"
    assert datos["prioridad"] == "Alta"


def test_eliminar_tarea(client):
    """CP05: Eliminar una tarea desaparece del listado."""
    crear = client.post(
        "/api/tareas",
        json={"nombre": "Para eliminar", "descripcion": "Desc", "prioridad": "Baja"},
    )
    tarea_id = crear.get_json()["id"]

    respuesta = client.delete(f"/api/tareas/{tarea_id}")
    assert respuesta.status_code == 200

    listado = client.get("/api/tareas").get_json()
    assert not any(t["id"] == tarea_id for t in listado)


def test_cambiar_estado(client):
    """CP06: Cambiar estado se actualiza correctamente."""
    crear = client.post(
        "/api/tareas",
        json={"nombre": "Estado", "descripcion": "Desc", "prioridad": "Media"},
    )
    tarea_id = crear.get_json()["id"]

    respuesta = client.patch(
        f"/api/tareas/{tarea_id}/estado", json={"estado": "Terminada"}
    )
    assert respuesta.status_code == 200
    assert respuesta.get_json()["estado"] == "Terminada"

    # Volver a pendiente
    respuesta = client.patch(
        f"/api/tareas/{tarea_id}/estado", json={"estado": "Pendiente"}
    )
    assert respuesta.status_code == 200
    assert respuesta.get_json()["estado"] == "Pendiente"


def test_seleccionar_prioridad(client):
    """CP07: Seleccionar prioridad se guarda correctamente."""
    respuesta = client.post(
        "/api/tareas",
        json={"nombre": "Prioridad", "descripcion": "Desc", "prioridad": "Baja"},
    )
    assert respuesta.status_code == 201
    assert respuesta.get_json()["prioridad"] == "Baja"
