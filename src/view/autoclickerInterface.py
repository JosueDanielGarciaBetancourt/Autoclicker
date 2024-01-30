from PyQt6 import QtWidgets
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
        self.boton_repetir = None
        self.last_double_spin_box_value = None
        self.last_combo_box_value = None
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)
        self.detectarTeclaWindow = DialogWindowDetectarTecla(self)
        self.reduction_percentage = None
        self.toggleElement_text = None
        self.click_interval = None
        self.autoclicker = None
        self.initGUI()
        self.autoclicker_state = False

        # Recepcionar señales emitidas desde la clase
        self.event_listener_thread = EventListenerThread()
        self.event_listener_thread.tecla_detectada.connect(self.on_tecla_detectada)
        self.event_listener_thread.click_detectado.connect(self.on_click_detectado)
        self.event_listener_thread.start()
        self.event_listener_thread.finished.connect(self.on_thread_finished)

        self.tecla_activacion = None
        self.boton_activacion = None
        self.dialogWindow_open = False
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
              f"last_double_spin_box_value={last_double_spin_box_value}\n")

    def guardar_configuraciones(self):
        # Guardar el último valor seleccionado del ComboBox
        self.last_combo_box_value = self.mainWindow.comboBoxKey.currentText()
        self.settings.setValue("last_combo_box_value", self.last_combo_box_value)

        # Guardar el último valor del DoubleSpinBox
        self.last_double_spin_box_value = self.mainWindow.doubleSpinBoxInterval.value()
        self.settings.setValue("last_double_spin_box_value", float(self.last_double_spin_box_value))

        print(f"Guardando configuraciones: tecla_activacion = {self.last_combo_box_value}, "
              f"click_interval = {self.last_double_spin_box_value}\n")

    def on_tecla_detectada(self, tecla):
        if not self.dialogWindow_open:
            tecla = tecla.upper()
            if not self.autoclicker_state:
                self.tecla_activacion = self.mainWindow.comboBoxKey.currentText()
                self.reduction_percentage = 0.8
                print(f"Tecla detectada main window: {tecla}")
                if self.tecla_activacion == tecla:
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
        try:
            if not self.dialogWindow_open:
                if not button == "Button.left":
                    self.reduction_percentage = 0.9
                    self.boton_activacion = self.mainWindow.comboBoxKey.currentText()
                    print(f"\nTecla detectada main window: {button}")
                    if not self.autoclicker_state:
                        if self.boton_activacion == button:
                            self.empezar()
                    else:
                        if self.boton_activacion == button:
                            print(f"\nSe presionó de nuevo la tecla de activación/pausa: {button}")
                            self.pausar()
                        else:
                            print("\nTecla incorrecta para pausar autoclicker")
        except Exception as e:
            print(e)

    def mostrar(self):
        self.show()

    def closeEvent(self, event):
        try:
            self.event_listener_thread.terminate_thread()
            self.guardar_configuraciones()
            self.pausar()  # Pausa el autoclicker antes de cerrar la ventana
        except Exception as e:
            print("Error al detener listeners o pausar autoclicker:", e)
        finally:
            self.close()

    def irInicio(self):
        self.mainWindow.stackedWidget.setCurrentIndex(1)

    def irAcercaDe(self):
        self.mainWindow.stackedWidget.setCurrentIndex(0)

    def pausar_listener_mainWindow(self):
        self.event_listener_thread.pausar_listener()

    def reactivar_listener_mainWindow(self):
        self.event_listener_thread.reactivar_listener()

    def mostrarVentanaAuxiliar(self):
        if not self.autoclicker_state:
            self.dialogWindow_open = True
            self.pausar_listener_mainWindow()
            self.detectarTeclaWindow.mostrar()

    def obtenerTeclaClickDetectado(self, detected_element):
        try:
            if self.dialogWindow_open:
                combo_box = self.mainWindow.comboBoxKey
                if detected_element == "Button.left":
                    mensaje = f"No se permite a {detected_element} como tecla de activación."
                    print(mensaje)
                    MensajesWindow.mostrarMensajeAdvertencia(mensaje)
                elif combo_box.findText(detected_element) == -1:
                    self.agregarTeclaDetectadaComboBox(detected_element)
                else:
                    print(f"El elemento {detected_element} ya se encuentra registrado en el QComboBox.")
            self.reactivar_listener_mainWindow()
            self.dialogWindow_open = False
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
            elif not self.autoclicker_state:  # Si está apagado
                print("\nEMPEZAR")
                self.autoclicker_state = True
                self.toggleElement_text = self.mainWindow.comboBoxKey.currentText()
                self.boton_repetir = self.mainWindow.comboBoxRepeatKey.currentText()
                print(f"Intervalo de click: {self.click_interval}")
                print(f"Elemento de activación: {self.toggleElement_text}")
                print(f"Botón a repetir: {self.boton_repetir}")
                if not self.autoclicker:
                    self.autoclicker = AutoClicker()
                    self.autoclicker.actualizarDatos(self.click_interval, self.toggleElement_text,
                                                     self.reduction_percentage, self.boton_repetir)
                    self.autoclicker.iniciarHilo()
                else:
                    self.autoclicker.actualizarDatos(self.click_interval, self.toggleElement_text,
                                                     self.reduction_percentage, self.boton_repetir)
                    if self.toggleElement_text == self.autoclicker.activation_input:
                        self.autoclicker.iniciarHilo()
        except Exception as e:
            print("Error inesperado durante la ejecución del autoclicker: ", e)

    def pausar(self):
        try:
            if self.autoclicker_state:
                self.autoclicker_state = False
                self.autoclicker.pausarHilo()
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

    def on_thread_finished(self):
        print("El hilo ha finalizado.\n")


class DialogWindowDetectarTecla(QtWidgets.QDialog):
    def __init__(self, parent=None):
        try:
            super().__init__(parent)
            self.detectarTeclaWindow = Ui_dialogDetectarTecla()
            self.detectarTeclaWindow.setupUi(self)
            self.parent = parent
            self.event_listener_thread2 = EventListenerThread()
            self.event_listener_thread2.tecla_detectada.connect(self.on_tecla_detectada)
            self.event_listener_thread2.click_detectado.connect(self.on_click_detectado)

        except Exception as e:
            print(e)

    def mostrar(self):
        self.show()
        self.event_listener_thread2.start()

    def closeEvent(self, event):
        self.event_listener_thread2.pausar_listener()
        self.close()

    def on_tecla_detectada(self, tecla):
        tecla = tecla.upper()
        print(f"\nTecla detectada en dialog: {tecla}")
        self.parent.obtenerTeclaClickDetectado(tecla)
        self.close()

    def on_click_detectado(self, button):
        if button == "Button.left":
            return
        else:
            print(f"\nBotón de mouse detectado en dialog: {button}")
            self.parent.obtenerTeclaClickDetectado(button)
            self.close()


class EventListenerThread(QThread):
    tecla_detectada = pyqtSignal(str)
    click_detectado = pyqtSignal(str)

    def __init__(self):
        super(EventListenerThread, self).__init__()
        self.keyboard_listener = None
        self.mouse_listener = None
        self.pressed_keys = set()
        self.pressed_buttons = set()
        self.pause_requested = False  # Nuevo atributo

    def run(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press,
                                                   on_release=self.on_release)
        self.mouse_listener = mouse.Listener(on_click=self.on_click)

        self.keyboard_listener.start()
        self.mouse_listener.start()

    def on_press(self, key):
        try:
            if self.pause_requested:
                return

            if hasattr(key, 'char'):
                tecla = key.char
            else:
                tecla = str(key)

            if tecla not in self.pressed_keys:
                self.tecla_detectada.emit(tecla)
                self.pressed_keys.add(tecla)
        except Exception as e:
            print(f"Error en on_press: {e}")

    def on_release(self, key):
        try:
            if self.pause_requested:
                return

            if hasattr(key, 'char'):
                tecla = key.char
            else:
                tecla = str(key)

            self.pressed_keys.discard(tecla)
        except Exception as e:
            print(f"Error en on_release: {e}")

    def on_click(self, x, y, button, pressed):
        try:
            if self.pause_requested:
                return

            button_str = str(button)

            if pressed:
                if button_str not in self.pressed_buttons:
                    self.click_detectado.emit(button_str)
                    self.pressed_buttons.add(button_str)
            else:
                # print("Releasing click")
                self.pressed_buttons.discard(button_str)
        except Exception as e:
            print(f"Error en on_click: {e}")

    def pausar_listener(self):
        self.pause_requested = True
        print("Se pausó los listeners")

    def reactivar_listener(self):
        self.pause_requested = False

    def terminate_thread(self):
        try:
            self.keyboard_listener.stop()
            self.mouse_listener.stop()
            self.finished.emit()
        except Exception as e:
            print(f"Error al detener el hilo: {e}")
