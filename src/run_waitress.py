import sys
import os
from waitress import serve

# Asegurar que el directorio actual esté en el path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from app import app  # Importar después de modificar sys.path

serve(app, host='0.0.0.0', port=5000)
