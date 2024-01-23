# TODO: Corregir cuando detecta algún botón del mouse, que no inicie inmediatamente

from PyQt6 import QtWidgets
from src.view.autoclickerInterface import MainWindow
import sys
import os

# Añadir la ruta del proyecto al sys.path
directorio_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
print(directorio_proyecto)
sys.path.append(directorio_proyecto)

if __name__ == '__main__':
    try:
        # Iniciar app
        app = QtWidgets.QApplication(sys.argv)
        autoclickerApp = MainWindow()
        autoclickerApp.mostrar()
        sys.exit(app.exec())
    except Exception as e:
        print("Error inesperado en main.py: ", e)
