
class Motor:
    def __init__(self, modelo = "Nema17", tipo = "pap", estado = "Detenido", habilitado = False):
        self.modelo = modelo
        self.tipo = tipo
        self.estado = estado
        self.habilitado = habilitado
        self._description = "Motores Reciclados de impresoras"
        
    def cambiar_estado(self, nuevo_estado):
        if (self.habilitado):
            self.estado = nuevo_estado
        else:
            return 

    def set_descripcion(self, new_descripcion):
        self._description = new_descripcion

    def cambiar_habilitacion(self, enable):
        
        self.habilitado = not self.estado