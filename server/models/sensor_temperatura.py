   
class Sensor_temp:
    def __init__(self, sensor_id, temperatura, tiempo_muestra):
        self.sensor_id = sensor_id
        self._temperatura = temperatura
        self.tiempo_muestra = tiempo_muestra
        
    def leer_temperatura(self):
        return self.temperatura

    def tomar_muestra(self):
        # Actualiza los valores de temperatura al realizar
        # una lectura del sensor de temperatura desde el robot.
        # Actualmente no implementado, pero se podrá al retocar
        # el firmware del robot.
        pass