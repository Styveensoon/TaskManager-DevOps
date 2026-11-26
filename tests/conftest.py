import os
import sys

import pytest

# Agregar la raiz del proyecto al sys.path para que pytest pueda importar app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, init_db  # noqa: E402


@pytest.fixture
def client(tmp_path):
    """Cliente de pruebas con una base de datos SQLite temporal y aislada."""
    app.config["TESTING"] = True
    app.config["DB_PATH"] = str(tmp_path / "test_tasks.db")
    init_db()

    with app.test_client() as client:
        yield client
