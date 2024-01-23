import time
import threading
from PyQt6.QtCore import QObject
from pynput import mouse


class AutoClicker(QObject):

    def __init__(self):
        super(AutoClicker, self).__init__()
        self.click_thread = None
        self.clicking = False
        self.mouse_controller = mouse.Controller()
        self.activation_input = None  # Button.middle | H | Y | Button.right | etc
        self.click_interval = 0.05
        self.stop_click_thread = threading.Event()
        self.reduction_percentage = None

    def actualizarDatos(self, click_interval, toggleElement_text, reduction_percentage):
        self.click_interval = click_interval
        self.activation_input = toggleElement_text
        self.reduction_percentage = reduction_percentage
        print("\nActualizar datos obj autoclicker:")
        print("Intervalo de click: ", self.click_interval)
        print("Elemento de activación: ", self.activation_input)

    def iniciarHilo(self):
        self.stop_click_thread.clear()  # Resetea el evento de detención del hilo
        self.clicking = True
        # Inicia el hilo para la función de autoclick
        self.click_thread = threading.Thread(target=self.clicker)
        self.click_thread.start()

    def pausarHilo(self):
        self.clicking = False
        self.stop_click_thread.set()  # Indica al hilo que se detenga
        print("Autoclicker pausado")

    """def clicker(self):
        while True:
            if self.clicking:
                self.mouse_controller.click(mouse.Button.left, 1)
            time.sleep(self.click_interval)
    """

    def clicker(self):
        next_click_time = time.time()
        while not self.stop_click_thread.is_set():
            if self.clicking:
                self.mouse_controller.click(mouse.Button.left, 1)

                next_click_time += self.click_interval
                sleep_time = max(0, next_click_time - time.time())

                self.stop_click_thread.wait(timeout=sleep_time)

                # Calcula sleep_aux proporcional al click_interval
                sleep_aux = self.click_interval * self.reduction_percentage
                time.sleep(sleep_aux)
