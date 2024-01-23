from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon, QPixmap
from pynput import keyboard, mouse
from src.logic.autoclicker import AutoClicker
from src.view.windowMessages import MensajesWindow
from src.view.mainWindow import Ui_MainWindow
from src.view.dialogDetectarTecla import Ui_dialogDetectarTecla
from PyQt6.QtCore import QThread, pyqtSignal, QSettings
import os
import sys

if getattr(sys, 'frozen', False):
    directorio_actual = sys._MEIPASS
else:
    directorio_actual = os.path.dirname(os.path.abspath(__file__))

directorio_src = os.path.abspath(os.path.join(directorio_actual, os.pardir))
ruta_relativa_main_window = os.path.join("view", "mainWindow.ui")
ruta_completa_main_window = os.path.join(directorio_src, ruta_relativa_main_window)
ruta_relativa_dialog_window = os.path.join("view", "dialogDetectarTecla.ui")
ruta_completa_dialog_window = os.path.join(directorio_src, ruta_relativa_dialog_window)

print(f'directorio_src: {directorio_src}')
print(ruta_completa_main_window)
print(ruta_completa_dialog_window)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.last_double_spin_box_value = None
        self.last_combo_box_value = None
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.reduction_percentage = None
        self.toggleElement_text = None
        self.click_interval = None
        self.autoclicker = None
        # self.mainWindow = uic.loadUi(os.path.join(directorio_src, "view", "mainWindow.ui"))
        self.detectarTeclaWindow = None  # Objeto de la classe DialogWindowDetectarTecla
        self.initGUI()
        self.autoclicker_state = False
        self.event_listener_thread = EventListenerThread()
        self.event_listener_thread.tecla_detectada.connect(self.on_tecla_detectada)
        self.event_listener_thread.click_detectado.connect(self.on_click_detectado)
        self.event_listener_thread.start()
        self.tecla_activacion = None
        self.dialogWindow_state = False
        self.settings = QSettings("JosueELPAPI", "AutoclickerOriginal")
        self.cargar_configuraciones()

    def cargar_configuraciones(self):
        # Cargar valores previamente grabados
        last_combo_box_value = self.settings.value("last_combo_box_value")
        last_double_spin_box_value = self.settings.value("last_double_spin_box_value")

        # Configurar el ComboBox con el valor cargado
        if last_combo_box_value is not None:
            index = self.mainWindow.comboBoxKey.findText(str(last_combo_box_value))
            if index != -1:
                self.mainWindow.comboBoxKey.setCurrentIndex(index)
            else:
                self.agregarTeclaDetectadaComboBox(last_combo_box_value)

        # Configurar el DoubleSpinBox con el valor cargado
        if last_double_spin_box_value is not None:
            self.mainWindow.doubleSpinBoxInterval.setValue(float(last_double_spin_box_value))

        # Imprimir mensajes de depuración
        print(f"Cargando configuraciones: last_combo_box_value={last_combo_box_value}, "
              f"last_double_spin_box_value={last_double_spin_box_value}")

    def guardar_configuraciones(self):
        # Guardar el último valor seleccionado del ComboBox
        self.last_combo_box_value = self.mainWindow.comboBoxKey.currentText()
        self.settings.setValue("last_combo_box_value", self.last_combo_box_value)

        # Guardar el último valor del DoubleSpinBox
        self.last_double_spin_box_value = self.mainWindow.doubleSpinBoxInterval.value()
        self.settings.setValue("last_double_spin_box_value", float(self.last_double_spin_box_value))

        print(f"Guardando configuraciones: tecla_activacion={self.last_combo_box_value}, "
              f"click_interval={self.last_double_spin_box_value}")

    def on_tecla_detectada(self, tecla):
        if not self.dialogWindow_state:
            tecla = tecla.upper()
            if not self.autoclicker_state:
                self.tecla_activacion = tecla
                self.reduction_percentage = 0.8
                print(f"Tecla detectada main window: {self.tecla_activacion}")
                texto_combobox = self.mainWindow.comboBoxKey.currentText()
                if self.tecla_activacion == texto_combobox:
                    print(f"Se presionó la tecla de activación/pausa: {self.tecla_activacion}")
                    self.empezar()
            else:
                print(f"Tecla detectada main window: {tecla}")
                if self.tecla_activacion == tecla:
                    print(f"Se presionó de nuevo la tecla de activación/pausa: {tecla}")
                    self.pausar()
                else:
                    print("Tecla incorrecta para pausar autoclicker")

    def on_click_detectado(self, button):
        if not self.dialogWindow_state:
            if not button == "Button.left":
                if not self.autoclicker_state:
                    self.tecla_activacion = button
                    self.reduction_percentage = 0.9
                    print(f"Clic detectado  main window: {button}")
                    texto_combobox = self.mainWindow.comboBoxKey.currentText()
                    if button == texto_combobox:
                        print(f"Se presionó el click de activación: {button}")
                        self.empezar()
                else:
                    print(f"Tecla detectada main window: {button}")
                    if self.tecla_activacion == button:
                        print(f"Se presionó de nuevo la tecla de activación/pausa: {button}")
                        self.pausar()
                    else:
                        print("Tecla incorrecta para pausar autoclicker")

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.close()

    def closeEvent(self, event):
        try:
            self.guardar_configuraciones()
            self.event_listener_thread.terminate()
            self.pausar()  # Pausa el autoclicker antes de cerrar la ventana
        except Exception as e:
            print("Error al detener listeners o pausar autoclicker:", e)
        finally:
            self.close()

    def irInicio(self):
        self.mainWindow.stackedWidget.setCurrentIndex(1)

    def irAcercaDe(self):
        self.mainWindow.stackedWidget.setCurrentIndex(0)

    def mostrarVentanaAuxiliar(self):
        self.dialogWindow_state = True
        if not self.detectarTeclaWindow:
            self.detectarTeclaWindow = DialogWindowDetectarTecla(self)
        self.detectarTeclaWindow.mostrar()

    def obtenerTeclaClickDetectado(self, detected_element):
        try:
            if self.dialogWindow_state:
                combo_box = self.mainWindow.comboBoxKey
                if detected_element == "Button.left":
                    mensaje = f"No se permite a {detected_element} como tecla de activación."
                    print(mensaje)
                    self.dialogWindow_state = False
                    MensajesWindow.mostrarMensajeAdvertencia(mensaje)
                elif combo_box.findText(detected_element) == -1:
                    self.agregarTeclaDetectadaComboBox(detected_element)
                else:
                    print(f"El elemento {detected_element} ya se encuentra registrado en el QComboBox.")
            self.dialogWindow_state = False
        except Exception as e:
            print("Error inesperado durante la obtención de la tecla/click detectado", e)

    def agregarTeclaDetectadaComboBox(self, detected_element):
        self.mainWindow.comboBoxKey.addItem(str(detected_element))
        last_index = self.mainWindow.comboBoxKey.count() - 1
        self.mainWindow.comboBoxKey.setCurrentIndex(last_index)

    def empezar(self):
        try:
            self.click_interval = self.mainWindow.doubleSpinBoxInterval.value()
            if self.click_interval <= 0:
                mensaje = "Seleccione un intervalo de click mayor a 0"
                print(mensaje)
                MensajesWindow.mostrarMensajeAdvertencia(mensaje)
            elif not self.autoclicker_state:
                print("\nEMPEZAR")
                self.autoclicker_state = True
                self.toggleElement_text = self.mainWindow.comboBoxKey.currentText()
                print(f"Intervalo de click: {self.click_interval}")
                print(f"Elemento de activación: {self.toggleElement_text}")

                if not self.autoclicker:
                    self.autoclicker = AutoClicker()
                    self.autoclicker.actualizarDatos(self.click_interval, self.toggleElement_text,
                                                     self.reduction_percentage)
                    self.autoclicker.iniciarHilo()
                else:
                    self.autoclicker.actualizarDatos(self.click_interval, self.toggleElement_text,
                                                     self.reduction_percentage)
                    if self.toggleElement_text == self.autoclicker.activation_input:
                        self.autoclicker.iniciarHilo()
        except Exception as e:
            print("Error inesperado durante la ejecución del autoclicker: ", e)

    def pausar(self):
        try:
            if self.autoclicker_state:
                print("\nPAUSAR")
                self.autoclicker.pausarHilo()
            else:
                print("\nPAUSAR")
            self.autoclicker_state = False
        except Exception as e:
            print("Error inesperado durante la pausa del autoclicker: ", e)

    def initGUI(self):
        try:
            self.mainWindow.stackedWidget.setCurrentIndex(1)

            # menubar
            self.mainWindow.actionInicio.triggered.connect(self.irInicio)
            self.mainWindow.actionAcercaDe.triggered.connect(self.irAcercaDe)

            # botones
            self.mainWindow.pushButtonDetectarTecla.clicked.connect(self.mostrarVentanaAuxiliar)
            self.mainWindow.pushButtonEmpezar.clicked.connect(self.empezar)
            self.mainWindow.pushButtonPausar.clicked.connect(self.pausar)
        except Exception as e:
            print(e)


class DialogWindowDetectarTecla(QtWidgets.QDialog):
    def __init__(self, parent=None):
        try:
            super(DialogWindowDetectarTecla, self).__init__(parent)
            self.detectarTeclaWindow = Ui_dialogDetectarTecla()
            self.detectarTeclaWindow.setupUi(self)
            self.parent = parent
            # self.detectarTeclaWindow = uic.loadUi(os.path.join(directorio_src, "view", "dialogDetectarTecla.ui"))
            self.event_listener_thread = EventListenerThread()
            self.event_listener_thread.start()
            self.initGUI()
        except Exception as e:
            print(e)

    def mostrar(self):
        self.show()
        self.event_listener_thread.start()

    def ocultar(self):
        self.close()  # Cerrar la ventana

    def closeEvent(self, event):
        self.close()

    def initGUI(self):
        self.event_listener_thread.tecla_detectada.connect(self.on_tecla_detectada)
        self.event_listener_thread.click_detectado.connect(self.on_click_detectado)

    def on_tecla_detectada(self, tecla):
        # Manejar la tecla detectada
        tecla = tecla.upper()
        print(f"Tecla detectada en dialog: {tecla}")
        self.parent.obtenerTeclaClickDetectado(tecla)
        self.close()

    def on_click_detectado(self, button):
        # Manejar el clic detectado
        print(f"Clic detectado en dialog: {button}")
        self.parent.obtenerTeclaClickDetectado(button)
        self.close()


class EventListenerThread(QThread):
    tecla_detectada = pyqtSignal(str)
    click_detectado = pyqtSignal(str)

    def __init__(self):
        super(EventListenerThread, self).__init__()
        self.activation_input = None
        self.deteccion_activa = True
        self.keyboard_listener = None
        self.mouse_listener = None

    def run(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        self.mouse_listener = mouse.Listener(on_click=self.on_click)

        self.keyboard_listener.start()
        self.mouse_listener.start()

    def on_press(self, key):
        try:
            if hasattr(key, 'char'):  # Verifica si la tecla tiene un atributo 'char'
                tecla = key.char
            else:
                tecla = str(key)

            self.tecla_detectada.emit(tecla)

        except Exception as e:
            print(f"Error en on_press: {e}")

    def on_click(self, x, y, button, pressed):
        try:
            if pressed:
                self.click_detectado.emit(str(button))

        except Exception as e:
            print(f"Error en on_click: {e}")


