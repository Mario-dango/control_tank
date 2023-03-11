import xml.etree.ElementTree as ET
from datetime import datetime
import os


class ArchivoModel:
    def __init__(self, archivoXml, main = False):
        self.archivoXml = archivoXml
        # if main:
        try:
            if os.path.isfile(self.archivoXml):
                # Carga el archivo existente y agrega nuevos registros
                self.tree = ET.parse(self.archivoXml)
                self.root = self.tree.getroot()
                ET.indent(self.root)
            else:
                # Crea un nuevo archivo XML en la carpeta "archivos"
                os.makedirs('archivos', exist_ok=True)
                self.root = ET.Element('logs')
                self.tree = ET.ElementTree(self.root)
                self.tree.write(self.archivoXml)
                ET.indent(self.root)
        except Exception as error:
            print("hubo un error al intentar ingresar al archivo xml: {}".format(error))
            
        # self.nuevo_log = ET.SubElement(self.root, 'log')

        self.logDate = ET.SubElement(self.root, "log")
        self.logDate.set('date', datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

        self.usuario = ET.SubElement(self.logDate, "usuario")
        self.usuario.text = "Local"

        self.conexion = ET.SubElement(self.logDate, "conectado")
        self.conexion.text = (datetime.now().strftime('%H:%M:%S'))

        self.acciones = ET.SubElement(self.logDate, "acciones")
        
    def agregar_accion(self, accion, tipo, parametro, texto):
        nueva_accion = ET.SubElement(self.acciones, "accion")
        nueva_accion.set("type", tipo)
        nueva_accion.set(accion, parametro)
        nueva_accion.text = texto
        ET.indent(self.root)
        self.tree.write(self.archivoXml)

    def agregar_conection(self, accion, texto):
        conection = ET.SubElement(self.user, accion)
        conection.text = texto

    def agregar_usuario(self, user, tipo, parametro,):
        usuarios = ET.SubElement(self.logDate, user)
        usuarios.set(tipo, parametro)

    def guardar_registro(self):
        try:
            self.desconectado = ET.SubElement(self.logDate, "desconectado")
            self.desconectado.text = (datetime.now().strftime('%H:%M:%S'))
            ET.indent(self.root)
            self.tree.write(self.archivoXml)
        except Exception as e:
            print("error al guardar: {}".format(e))

    def leer_archivo(self, otroXml=None):
        if otroXml == None:
            archivoXml = self.archivoXml
        else:
            archivoXml = otroXml
        listaDatos = []
        if archivoXml == "" or archivoXml == None:
            if len(listaDatos) == 0:
                listaDatos.append("No se definió el archivo a buscar.")
            else:
                listaDatos[0] = "No se definió el archivo a buscar."
            return listaDatos[:1]
        else:
            try:
                # Cargar el archivo XML en un objeto ElementTree
                tree = ET.parse(archivoXml)
                root = tree.getroot()
                # Recorrer los elementos de cada log y mostrar su información
                for log in root.findall('log'):
                    listaDatos.append('Fecha: ' + log.get('date'))
                    listaDatos.append('Usuario: ' + log.find('usuario').text)
                    listaDatos.append('Conexión: ' + log.find('conectado').text)
                    # Obtener una lista de todos los elementos 'acciones' en el archivo XML
                    acciones_lista = log.findall('.//acciones')
                    # Recorrer la lista de elementos 'acciones' e imprimir la información
                    for acciones in acciones_lista:
                        for accion in acciones.findall('*'):
                            listaDatos.append('Mensaje: ' + accion.text)
                            listaDatos.append('\tTipo de acción: ' + accion.get('type'))
                            if accion.get('type') == 'movimiento':
                                listaDatos.append('\tDuración: ' + accion.get('duration'))
                            elif accion.get('type') == 'motores' or accion.get('type') == 'bluetooth':
                                listaDatos.append('\tAcción: ' + accion.get('action'))   
                    try:                             
                        listaDatos.append('Desconexión:' + log.find('desconectado').text + '\n')
                    except Exception as e:
                        print(e)
            except FileNotFoundError as error:
                print("Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar.")
                if len(listaDatos) == 0:
                    listaDatos.append("Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar.")
                else:
                    listaDatos[0] = "Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar."
                return listaDatos[:1]
            return listaDatos
        
    def leerRegistro(self, otroXml=None):
        if otroXml == None:
            registroXml = self.archivoXml
        else:
            registroXml = otroXml
        listaDatos = []
        if registroXml == "" or registroXml == None:
            if len(listaDatos) == 0:
                listaDatos.append("No se definió el archivo a buscar.")
            else:
                listaDatos[0] = "No se definió el archivo a buscar."
            return listaDatos[:1]
        else:
            try:
                tree = ET.parse(registroXml)
                root = tree.getroot()
                # Recorrer los elementos de cada log y mostrar su información
                for log in root.findall('log'):                                
                    listaDatos.append('Fecha: ' + log.get('date') + ('\t->\tUsuario: ' + log.find('usuario').text))
            except FileNotFoundError as error:
                print("Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar.")
                if len(listaDatos) == 0:
                    listaDatos.append("Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar.")
                else:
                    listaDatos[0] = "Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar."
                return listaDatos[:1]
            return listaDatos
    
    def enviarXml (self):        
        try:
            with open(self.archivoXml, 'r') as f:
                activities = f.read()
            return activities
        except Exception as e:
            print("Hubo un error al abrir archivo: {}".format(e))