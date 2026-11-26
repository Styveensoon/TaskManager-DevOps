"""Pruebas de la funcionalidad RF03: editar tareas."""


def _crear_tarea(client, **extra):
    payload = {
        "nombre": "Tarea original",
        "descripcion": "Descripcion original",
        "prioridad": "Media",
        "estado": "Pendiente",
    }
    payload.update(extra)
    respuesta = client.post("/api/tareas", json=payload)
    assert respuesta.status_code == 201
    return respuesta.get_json()


def test_editar_todos_los_campos(client):
    tarea = _crear_tarea(client)

    respuesta = client.put(
        f"/api/tareas/{tarea['id']}",
        json={
            "nombre": "Tarea actualizada",
            "descripcion": "Nueva descripcion",
            "prioridad": "Alta",
            "estado": "En Proceso",
        },
    )

    assert respuesta.status_code == 200
    actualizada = respuesta.get_json()
    assert actualizada["nombre"] == "Tarea actualizada"
    assert actualizada["descripcion"] == "Nueva descripcion"
    assert actualizada["prioridad"] == "Alta"
    assert actualizada["estado"] == "En Proceso"


def test_edicion_parcial_conserva_campos(client):
    tarea = _crear_tarea(client)

    respuesta = client.put(
        f"/api/tareas/{tarea['id']}", json={"prioridad": "Baja"}
    )

    assert respuesta.status_code == 200
    actualizada = respuesta.get_json()
    assert actualizada["nombre"] == tarea["nombre"]
    assert actualizada["descripcion"] == tarea["descripcion"]
    assert actualizada["prioridad"] == "Baja"
    assert actualizada["estado"] == tarea["estado"]


def test_editar_limpia_espacios_del_nombre(client):
    tarea = _crear_tarea(client)

    respuesta = client.put(
        f"/api/tareas/{tarea['id']}", json={"nombre": "   Nombre limpio   "}
    )

    assert respuesta.status_code == 200
    assert respuesta.get_json()["nombre"] == "Nombre limpio"


def test_editar_con_nombre_vacio_es_rechazado(client):
    tarea = _crear_tarea(client)

    respuesta = client.put(f"/api/tareas/{tarea['id']}", json={"nombre": "   "})

    assert respuesta.status_code == 400
    # La tarea original no se modifica
    actual = client.get(f"/api/tareas/{tarea['id']}").get_json()
    assert actual["nombre"] == tarea["nombre"]


def test_editar_tarea_inexistente(client):
    respuesta = client.put("/api/tareas/9999", json={"nombre": "No existe"})
    assert respuesta.status_code == 404
