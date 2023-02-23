import xml.etree.ElementTree as ET
from datetime import datetime

class ArchivoModel:
    def __init__(self):
        self.root = ET.Element('registro_actividad')
        self.general = ET.SubElement(self.root, 'datos_generales')
        self.robot = ET.SubElement(self.general, 'robot')
        self.cliente = ET.SubElement(self.general, 'cliente')
        self.usos = ET.SubElement(self.root, 'usos')
        self.acciones = ET.SubElement(self.root, 'acciones')

    def agregar_datos_generales(self, tipo, nombre, autor):
        if tipo == "robot":
            self.robot.set('nombre', nombre)
            self.robot.set('autor', autor)
        elif tipo == "cliente":
            self.cliente.set('nombre', nombre)

    def agregar_uso(self, usuario, fecha_hora):
        uso = ET.SubElement(self.usos, 'uso')
        uso.set('usuario', usuario)
        uso.set('fecha_hora', fecha_hora)

    def agregar_accion(self, accion, parametros, tiempo):
        registro = ET.SubElement(self.acciones, 'registro')
        registro.set('fecha_hora', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        registro.set('tiempo', str(tiempo))
        accion_element = ET.SubElement(registro, 'accion')
        accion_element.text = accion
        parametros_element = ET.SubElement(registro, 'parametros')
        parametros_element.text = parametros

    def guardar_registro(self, archivo):
        tree = ET.ElementTree(self.root)
        tree.write(archivo)

    def leer_registro(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()
        robot_nombre = root.find('.//robot').get('nombre')
        robot_autor = root.find('.//robot').get('autor')
        cliente_nombre = root.find('.//cliente').get('nombre')
        usos = []
        for uso in root.findall('.//uso'):
            usos.append({
                'usuario': uso.get('usuario'),
                'fecha_hora': uso.get('fecha_hora')
            })
        acciones = []
        for registro in root.findall('.//registro'):
            acciones.append({
                'fecha_hora': registro.get('fecha_hora'),
                'tiempo': float(registro.get('tiempo')),
                'accion': registro.find('accion').text,
                'parametros': registro.find('parametros').text
            })
        return {
            'robot_nombre': robot_nombre,
            'robot_autor': robot_autor,
            'cliente_nombre': cliente_nombre,
            'usos': usos,
            'acciones': acciones
        }
