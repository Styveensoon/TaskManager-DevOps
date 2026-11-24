import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", template_folder="templates")

# Ruta absoluta de la base de datos SQLite (funciona en local y en despliegue)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "tasks.db")


def get_db_connection():
    import sqlite3

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT DEFAULT '',
            prioridad TEXT NOT NULL DEFAULT 'Media',
            estado TEXT NOT NULL DEFAULT 'Pendiente',
            fecha_creacion TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


# Crear la tabla al iniciar la aplicación
init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/tareas", methods=["GET"])
def listar_tareas():
    conn = get_db_connection()
    tareas = conn.execute(
        "SELECT * FROM tareas ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return jsonify([dict(t) for t in tareas])


@app.route("/api/tareas", methods=["POST"])
def crear_tarea():
    data = request.get_json(silent=True) or {}
    nombre = (data.get("nombre") or "").strip()
    descripcion = (data.get("descripcion") or "").strip()
    prioridad = data.get("prioridad") or "Media"
    estado = data.get("estado") or "Pendiente"

    if not nombre:
        return jsonify({"error": "El nombre de la tarea es obligatorio"}), 400

    if prioridad not in ("Alta", "Media", "Baja"):
        prioridad = "Media"
    if estado not in ("Pendiente", "En Proceso", "Terminada"):
        estado = "Pendiente"

    conn = get_db_connection()
    cur = conn.execute(
        """
        INSERT INTO tareas (nombre, descripcion, prioridad, estado, fecha_creacion)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nombre, descripcion, prioridad, estado, datetime.now().isoformat()),
    )
    tarea_id = cur.lastrowid
    conn.commit()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    conn.close()
    return jsonify(dict(tarea)), 201


@app.route("/api/tareas/<int:tarea_id>", methods=["GET"])
def obtener_tarea(tarea_id):
    conn = get_db_connection()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    conn.close()
    if tarea is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(dict(tarea))


@app.route("/api/tareas/<int:tarea_id>", methods=["PUT"])
def editar_tarea(tarea_id):
    data = request.get_json(silent=True) or {}
    conn = get_db_connection()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    if tarea is None:
        conn.close()
        return jsonify({"error": "Tarea no encontrada"}), 404

    nombre = (data.get("nombre") or tarea["nombre"] or "").strip()
    descripcion = data.get("descripcion", tarea["descripcion"])
    prioridad = data.get("prioridad", tarea["prioridad"])
    estado = data.get("estado", tarea["estado"])

    if not nombre:
        conn.close()
        return jsonify({"error": "El nombre de la tarea es obligatorio"}), 400
    if prioridad not in ("Alta", "Media", "Baja"):
        prioridad = "Media"
    if estado not in ("Pendiente", "En Proceso", "Terminada"):
        estado = "Pendiente"

    conn.execute(
        """
        UPDATE tareas
        SET nombre = ?, descripcion = ?, prioridad = ?, estado = ?
        WHERE id = ?
        """,
        (nombre, descripcion, prioridad, estado, tarea_id),
    )
    conn.commit()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    conn.close()
    return jsonify(dict(tarea))


@app.route("/api/tareas/<int:tarea_id>/estado", methods=["PATCH"])
def cambiar_estado(tarea_id):
    data = request.get_json(silent=True) or {}
    estado = data.get("estado")
    if estado not in ("Pendiente", "En Proceso", "Terminada"):
        return jsonify({"error": "Estado invalido"}), 400

    conn = get_db_connection()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    if tarea is None:
        conn.close()
        return jsonify({"error": "Tarea no encontrada"}), 404
    conn.execute(
        "UPDATE tareas SET estado = ? WHERE id = ?", (estado, tarea_id)
    )
    conn.commit()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    conn.close()
    return jsonify(dict(tarea))


@app.route("/api/tareas/<int:tarea_id>", methods=["DELETE"])
def eliminar_tarea(tarea_id):
    conn = get_db_connection()
    tarea = conn.execute("SELECT * FROM tareas WHERE id = ?", (tarea_id,)).fetchone()
    if tarea is None:
        conn.close()
        return jsonify({"error": "Tarea no encontrada"}), 404
    conn.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
    conn.commit()
    conn.close()
    return jsonify({"ok": True, "mensaje": "Tarea eliminada"})


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(BASE_DIR, "static"), "favicon.ico", mimetype="image/x-icon"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
