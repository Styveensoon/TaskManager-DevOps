import sys
import os

# Agregar la raiz del proyecto al sys.path para que pytest pueda importar app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
