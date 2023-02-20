import time
import serial

# Configura la conexión serial con el módulo HC-06
ser = serial.Serial('COM16', 9600) # Reemplaza 'COMX' con el puerto serial que corresponda

# Espera a que se establezca la conexión serial
while not ser.is_open:
    time.sleep(1)

# Obtiene el tiempo inicial
initial_time = time.time()

# Envía el tiempo transcurrido cada 5 segundos
while True:
    elapsed_time = int(time.time() - initial_time) # Calcula el tiempo transcurrido desde la conexión
    data = str(elapsed_time) + '\n' # Agrega un salto de línea al final para indicar el fin del mensaje
    ser.write(data.encode()) # Envía el tiempo transcurrido por Bluetooth
    time.sleep(5) # Espera 5 segundos antes de enviar el siguiente mensaje
