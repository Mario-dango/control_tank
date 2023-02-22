import datetime
import random
class Sensor_temp:
    def __init__(self, sensor_id, temperatura):
        self.sensor_id = sensor_id
        self._temperatura = temperatura
        self.muestras = {}
        
    def leer_temperatura(self):
        return float(self._temperatura)

    def tomar_muestra(self):
        # Actualiza los valores de temperatura al realizar
        # una lectura del sensor de temperatura desde el robot.
        # Actualmente no implementado, pero se podrá al retocar
        # el firmware del robot.
        # self._temperatura = nueva temp
        nueva_temp = round(random.uniform(10, 50), 2)
        ultimaMuestraTomada = datetime.datetime.now()
        self.muestras[ultimaMuestraTomada:nueva_temp]
    