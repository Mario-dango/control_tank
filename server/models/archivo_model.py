import xml.etree.ElementTree as ET
from datetime import datetime

class ArchivoModel:
    def __init__(self):
        self.root = ET.Element('logs')
        self.logDate = ET.SubElement(self.root, "logs")
        self.logDate.set('fecha', datetime.now().strftime('%d-%m-%Y'))

        self.user = ET.SubElement(self.logDate, 'usuario')
        # self.user.set("type", "local")
        self.conectado = ET.SubElement(self.user, 'conectado')
        self.conectado.text = datetime.now().strftime("%H:%M:%S")

        self.acciones = ET.SubElement(self.user, 'acciones')

        self.bluetooth = ET.SubElement(self.acciones, 'bluetooth')
        self.bluetooth.set("acción", "on")
        self.motores = ET.SubElement(self.acciones, 'motores')
        self.motores.set("motores", "on")
        self.movimientor = ET.SubElement(self.acciones, 'movimiento')
        self.motores.set("duración", "0.43")
        self.motores.text = "Avanzar"

        self.desconectado = ET.SubElement(self.user, 'desconectado')
        self.desconectado.text = datetime.now().strftime("%H:%M:%S")


    def agregar_accion(self, accion, tipo, parametro, texto):
        acciones = ET.SubElement(self.acciones, accion)
        acciones.set(tipo, parametro)
        acciones.text = texto

    def agregar_conection(self, accion, texto):
        conection = ET.SubElement(self.user, accion)
        conection.text = texto

    def agregar_usuario(self, user, tipo, parametro,):
        usuarios = ET.SubElement(self.logDate, user)
        usuarios.set(tipo, parametro)

    def guardar_registro(self, archivo):
        tree = ET.ElementTree(self.root)
        tree.write(archivo)

    def leer_archivo(self, archivo):
        listaDatos = []
        if archivo == "" or archivo == None:
            if len(listaDatos) == 0:
                listaDatos.append("No se definió el archivo a buscar.")
            else:
                listaDatos[0] = "No se definió el archivo a buscar."
            return listaDatos[:1]
        else:
            try:
                # /home/bawy/Plantillas/git_poo/control_tank/server/archivos/log.xml
                #   Ruta relativa si se ejecuta desde control_tank -> control_tank/server/archivos/log.xml
                # Cargar el archivo XML en un objeto ElementTree
                tree = ET.parse(archivo)
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
                    listaDatos.append('Desconexión:' + log.find('desconectado').text + '\n')
            except FileNotFoundError as error:
                print("Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar.")
                if len(listaDatos) == 0:
                    listaDatos.append("Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar.")
                else:
                    listaDatos[0] = "Ha ocurrido un error: {}".format(error) + "\nEl archivo no existe o no se logró encontrar."
                return listaDatos[:1]
            return listaDatos
        
    def leerRegistro(self, archivo):
        listaDatos = []
        if archivo == "" or archivo == None:
            if len(listaDatos) == 0:
                listaDatos.append("No se definió el archivo a buscar.")
            else:
                listaDatos[0] = "No se definió el archivo a buscar."
            return listaDatos[:1]
        else:
            try:
                tree = ET.parse(archivo)
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
    
    def enviarXml (self, archivoXml):        
        try:
            with open(archivoXml, 'r') as f:
                activities = f.read()
            return activities
        except Exception as e:
            print("Hubo un error al abrir archivo: {}".format(e))