"""Pruebas de la funcionalidad RF04: eliminar tareas."""


def _crear(client, nombre):
    respuesta = client.post("/api/tareas", json={"nombre": nombre, "prioridad": "Media"})
    assert respuesta.status_code == 201
    return respuesta.get_json()["id"]


def test_eliminar_tarea_desaparece_del_listado(client):
    tarea_id = _crear(client, "Tarea para eliminar")

    respuesta = client.delete(f"/api/tareas/{tarea_id}")

    assert respuesta.status_code == 200
    assert respuesta.get_json()["ok"] is True
    listado = client.get("/api/tareas").get_json()
    assert all(t["id"] != tarea_id for t in listado)


def test_eliminar_solo_la_tarea_seleccionada(client):
    id_uno = _crear(client, "Tarea uno")
    id_dos = _crear(client, "Tarea dos")

    client.delete(f"/api/tareas/{id_uno}")

    listado = client.get("/api/tareas").get_json()
    ids = [t["id"] for t in listado]
    assert id_uno not in ids
    assert id_dos in ids


def test_consultar_tarea_eliminada_devuelve_404(client):
    tarea_id = _crear(client, "Tarea eliminada")

    client.delete(f"/api/tareas/{tarea_id}")
    respuesta = client.get(f"/api/tareas/{tarea_id}")

    assert respuesta.status_code == 404


def test_eliminar_tarea_inexistente_devuelve_404(client):
    respuesta = client.delete("/api/tareas/9999")
    assert respuesta.status_code == 404
