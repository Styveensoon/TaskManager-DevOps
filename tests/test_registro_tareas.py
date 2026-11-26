"""Pruebas de la funcionalidad RF01: registrar tareas."""


def test_registro_completo(client):
    respuesta = client.post(
        "/api/tareas",
        json={
            "nombre": "Preparar informe DevOps",
            "descripcion": "Documentar las fases del ciclo",
            "prioridad": "Alta",
            "estado": "Pendiente",
        },
    )

    assert respuesta.status_code == 201
    tarea = respuesta.get_json()
    assert tarea["nombre"] == "Preparar informe DevOps"
    assert tarea["descripcion"] == "Documentar las fases del ciclo"
    assert tarea["prioridad"] == "Alta"
    assert tarea["estado"] == "Pendiente"
    assert tarea["fecha_creacion"]


def test_registro_limpia_espacios_del_nombre(client):
    respuesta = client.post(
        "/api/tareas",
        json={"nombre": "   Revisar tablero   ", "prioridad": "Media"},
    )

    assert respuesta.status_code == 201
    assert respuesta.get_json()["nombre"] == "Revisar tablero"


def test_registro_aparece_en_el_listado(client):
    client.post("/api/tareas", json={"nombre": "Tarea recien creada"})

    listado = client.get("/api/tareas").get_json()
    assert any(t["nombre"] == "Tarea recien creada" for t in listado)


def test_registro_sin_cuerpo_json(client):
    respuesta = client.post("/api/tareas", data="no es json", content_type="text/plain")

    assert respuesta.status_code == 400
    assert "nombre" in respuesta.get_json()["error"].lower()
