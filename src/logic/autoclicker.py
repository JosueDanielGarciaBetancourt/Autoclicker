import time
import threading
from PyQt6.QtCore import QObject
from pynput import mouse, keyboard


class AutoClicker(QObject):

    def __init__(self):
        super(AutoClicker, self).__init__()
        self.click_thread = None
        self.clicking = False
        self.mouse_controller = mouse.Controller()
        self.keyboard_controller = keyboard.Controller()
        self.activation_input = None  # Button.middle | H | Y | Button.right | etc
        self.click_interval = 0.05
        self.stop_click_thread = threading.Event()
        self.reduction_percentage = None
        self.boton_repetir = None

    def actualizarDatos(self, click_interval, toggleElement_text, reduction_percentage, boton_repetir):
        try:
            self.click_interval = click_interval
            self.activation_input = toggleElement_text
            self.reduction_percentage = reduction_percentage
            if boton_repetir == "Button.left":
                self.boton_repetir = mouse.Button.left
            elif boton_repetir == "Button.right":
                self.boton_repetir = mouse.Button.right
            elif boton_repetir == "KEY.SHIFT":
                self.boton_repetir = keyboard.Key.shift
            else:
                print("No se pudo escoger el botón a repetir")
            # print("\nActualizar datos obj autoclicker:")
            # print("Intervalo de click: ", self.click_interval)
            # print("Elemento de activación: ", self.activation_input)
        except Exception as e:
            print("Error inesperado durante la asignación de datos al autoclicker",e)

    def iniciarHilo(self):
        self.stop_click_thread.clear()  # Resetea el evento de detención del hilo
        self.clicking = True
        # Inicia el hilo para la función de autoclick
        self.click_thread = threading.Thread(target=self.clicker)
        self.click_thread.start()
        print("Autoclicker iniciado")

    def pausarHilo(self):
        self.clicking = False
        self.stop_click_thread.set()  # Indica al hilo que se detenga
        print("Autoclicker pausado")

    def clicker(self):
        next_click_time = time.time()
        while not self.stop_click_thread.is_set():
            if self.clicking:
                if self.boton_repetir == keyboard.Key.shift:
                    self.keyboard_controller.press(self.boton_repetir)
                    time.sleep(self.click_interval)  # Ajusta el tiempo según sea necesario
                    self.keyboard_controller.release(self.boton_repetir)
                    time.sleep(self.click_interval)
                else:
                    self.mouse_controller.click(self.boton_repetir, 1)
                    next_click_time += self.click_interval
                    sleep_time = max(0, next_click_time - time.time())

                    self.stop_click_thread.wait(timeout=sleep_time)

                    # Calcula sleep_aux proporcional al click_interval
                    sleep_aux = self.click_interval * self.reduction_percentage
                    time.sleep(sleep_aux)

