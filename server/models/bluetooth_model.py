import serial
import time
class BlueRobot:
    def __init__(self, port = "Nada", baudrate = 9600):
        self._port = port
        self._baudrate = baudrate
        self.serial = None
        
    def changePort(self, newPort):
        self._port = newPort
        return
        
    def changeBaudrate(self, newBaudrate):
        self._baudrate = newBaudrate
        return

    def connect(self):
        print(self._port)
        print(type(self._port))
        print(self._baudrate)
        print(type(self._baudrate))
        try:
            if self.serial is not None and self.serial.isOpen():
                print(f"El puerto {self._port} ya está conectado")
                return True
            self.serial = serial.Serial(self._port, self._baudrate)
            # Espera a que se establezca la conexión serial
            while not self.serial.isOpen():
                time.sleep(0.1)
            print(f"Conectado al puerto {self._port} con velocidad de transmisión {self._baudrate}")
            return True
        except serial.SerialException as e:
            print(f"No se pudo conectar al puerto {self._port}: {e}")
            return False

    def disconnect(self):
        try:
            if self.serial is not None and self.serial.isOpen():
                self.serial.close()
                print(f"Desconectado del puerto {self._port}")
                return True
            else:
                print("El puerto serie no está conectado")
                return False
        except serial.SerialException as e:
            print(f"Error al desconectar del puerto {self._port}: {e}")

    def send(self, data):
        try:
            if self.serial is not None and self.serial.isOpen():
                print(f"Enviado: {data}")
                self.serial.write(data.encode())
            else:
                print("El puerto serie no está conectado")
        except serial.SerialException as e:
            print(f"Error al enviar datos al puerto {self._port}: {e}")
