from models.archivo_model import ArchivoModel
import re

class ArchivoController:
    def __init__(self, fromMain = False):
        self.modelo = ArchivoModel(archivoXml="archivos/log.xml", main=fromMain)

    def agregar_accion(self, accion, tipo, parametros, texto):
        #   accio: representa si es "action" o "duration"
        #   tipo: Representa si es "movimiento", "bluetooth" o "motores"
        #   parametros: Respresentan los valores para el elemento accio
        #   texto: Representa el contenido del elemento accion 
        if type(parametros) == float:
            strTime = str(round(parametros, 4))[:5]
            parametros = strTime
        self.modelo.agregar_accion(accion, tipo, parametros, texto)

    def agregar_conection(self, estado, texto):
        self.modelo.agregar_conection(estado, texto)

    def agregar_usuario(self, user, tipo, parametro,):
        self.modelo.agregar_usuario(user, tipo, parametro)

    def guardar_registro(self):
        self.modelo.guardar_registro()
        
    def leerXml(self, archivoXml, fecha="todas"):
        if fecha == "todas":
            return self.modelo.leer_archivo(otroXml= archivoXml)
        else:
            lista = self.modelo.leer_archivo(otroXml=archivoXml)
            fecha_inicial = fecha
            acciones = []

            encontrado = False
            for linea in lista:
                if linea.startswith("Fecha:"):
                    fecha = linea.split(": ")[1].strip()
                    if fecha == fecha_inicial:
                        encontrado = True
                        continue
                    elif encontrado:
                        break

                if encontrado and linea.startswith("Mensaje: "):
                    # Extraer la información que necesitas
                    acciones.append(linea.split(":")[-1].strip())

                elif encontrado and linea.startswith("\tTipo de acción: "):
                    # Extraer la información que necesitas
                    acciones.append(linea.split(":")[-1].strip())

                elif encontrado and linea.startswith("\tDuración: "):
                    # Extraer la información que necesitas
                    acciones.append(linea.split(":")[-1].strip())

                elif encontrado and linea.startswith("\tAcción: "):
                    # Extraer la información que necesitas
                    acciones.append(linea.split(":")[-1].strip())
            print(acciones)
            return acciones
     
    def registros(self, archivoXml):
        registros = self.modelo.leerRegistro(otroXml = archivoXml)
        if len(registros) != 0:
            for objetos in range(0,len(registros)):
                registros[objetos] = "[{}] ".format(objetos) + registros[objetos]
        return registros

    def leerBinaryXml(self):
        return self.modelo.enviarXml()

