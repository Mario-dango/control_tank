from models.archivo_model import ArchivoModel
import re

class ArchivoController:
    def __init__(self):
        self.modelo = ArchivoModel()

    def agregar_accion(self, accion, tipo, parametros, texto):
        if accion == "bluetooth":
            pass    # lógica de bluetooth
        elif accion == "motores":
            pass    # lógica de motores
        elif accion == "mover":
            pass    # lógica de movimiento
        else:
            pass    # Reporte de error
        self.modelo.agregar_accion(accion, tipo, parametros, texto)

    def agregar_conection(self, estado, texto):
        self.modelo.agregar_conection(estado, texto)

    def agregar_usuario(self, user, tipo, parametro,):
        self.modelo.agregar_usuario(user, tipo, parametro)

    def guardar_registro(self, archivo):
        self.modelo.guardar_registro(archivo)
        
    def leerXml(self, archivoXml, fecha="todas"):
        if fecha == "todas":
            return self.modelo.leer_archivo(archivo = archivoXml)
        else:
            lista = self.modelo.leer_archivo(archivo=archivoXml)
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
        registros = self.modelo.leerRegistro(archivo = archivoXml)
        if len(registros) != 0:
            for objetos in range(0,len(registros)):
                registros[objetos] = "[{}] ".format(objetos) + registros[objetos]
        return registros

    def leerBinaryXml(self, archivoXml):
        return self.modelo.enviarXml(archivoXml)

