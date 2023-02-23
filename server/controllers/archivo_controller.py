from models.archivo_model import ArchivoModel

class ArchivoController:
    def __init__(self):
        self.modelo = ArchivoModel()

    def agregar_datos_generales(self, tipo, nombre, autor=None):
        self.modelo.agregar_datos_generales(tipo, nombre, autor)

    def agregar_uso(self, usuario, fecha_hora):
        self.modelo.agregar_uso(usuario, fecha_hora)

    def agregar_accion(self, accion, parametros, tiempo):
        self.modelo.agregar_accion(accion, parametros, tiempo)

    def guardar_registro(self, archivo):
        self.modelo.guardar_registro(archivo)

    def leer_registro(self, archivo):
        return self.modelo.leer_registro(archivo)

