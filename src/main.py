from PyQt6 import QtWidgets
from src.view.autoclickerInterface import MainWindow
import sys

if __name__ == '__main__':
    try:
        # Iniciar app
        app = QtWidgets.QApplication(sys.argv)
        autoclickerApp = MainWindow()
        autoclickerApp.mostrar()
        sys.exit(app.exec())
    except Exception as e:
        print("Error inesperado en main.py: ", e)
