#define PY_SSIZE_T_CLEAN
import bluetooth
import time
import socket

class BlueRobot:
    def __init__(self, address = "20:16:04:18:35:40", port = 1):
        self._port = port
        self._address = address
            # Crear un objeto socket Bluetooth
        # self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        # self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.flagConnect = False
 
    def changeAddress(self, newAddress):
        print(newAddress)
        self._address = newAddress
        return

    def changeBaudrate(self, newBaudrate):
        self._address = newBaudrate
        return

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self._port = 1
            # Conectar el socket Bluetooth al dispositivo
            print(type(self._address))
            print(self._address)
            print(type(self._port))
            print(self._port)
            self.sock.connect((self._address, self._port))
            print(f"Conectado al puerto {self._port} con velocidad de transmisión {self._address}")
            self.flagConnect = True
            return True
        except bluetooth.BluetoothError as e:
            print(f"No se pudo conectar al puerto {self._port}: {e}")
            return False

    def disconnect(self):
        try:
            if self.flagConnect is True:
                self.sock.close()
                self.sock = None
                print(f"Desconectado del puerto {self._port}")
                self.flagConnect = False
                return True
            else:
                print("El puerto serie no está conectado")
                self.flagConnect = False
                return False
        except bluetooth.BluetoothError as e:
            print(f"Error al desconectar del puerto {self._port}: {e}")

    def send(self, data):
        try:
            if self.flagConnect is not False:
                print(f"Enviado: {data}")
                self.sock.send(bytes(data, 'utf-8'))
            else:
                print("El puerto serie no está conectado")
        except bluetooth.BluetoothError as e:
            print(f"Error al enviar datos al puerto {self._port}: {e}")
