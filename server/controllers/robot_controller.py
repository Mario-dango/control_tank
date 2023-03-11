#define PY_SSIZE_T_CLEAN
from PyQt5.QtCore import QObject
from models.robot_bt import Robot
from controllers.archivo_controller import ArchivoController
from time import sleep, time
from datetime import datetime

class RobotControllerOptimizado(QObject):
    def __init__(self, mainView):
        super().__init__()
        self.view = mainView
        self.robot_tank = Robot()
        self.archivo = ArchivoController()
        # self.portBt = self.view.bt_list.currentText()
        self.addressBT = ""
        self.tiempoTotal = 0
        self.texto = ""
        self.startTime = 0
        self.endTime = 0
        self.acciones = []

    def conectarBluetooth(self, auto=False):
        self.addressBT = self.view.bt_list.currentText()
        print(self.addressBT)
        texto = ""
        estado = ""
        try:
            if self.addressBT != "":
                info = "Se presionó el botón de conectar/desconectar Serial Bluetooth."
                print(info)
                self.view.add_rlog(info)
                if not self.robot_tank.estado_bt:
                    self.robot_tank.conectar_bluetooth(self.addressBT)
                    estado = "on"
                    texto = "Activar conexion bluetooth"
                else:
                    self.robot_tank.estado_bt = False
                    self.robot_tank.bluetooth.disconnect()
                    estado = "off"
                    texto = "Desactivar conexion bluetooth"
        except TypeError as e:
            print("Se produjo un error al intentar conectar al bluetooth: {}".format(e))            
            return False
        
        if not auto:
            self.archivo.agregar_accion(accion="action", parametros=estado, tipo="bluetooth" ,texto=texto)
            

    def habilitar_motores(self, auto=False, exit=False): 
        print(self.view.on_off_motor.isChecked()) 
        texto = ""
        estado = ""
        try:
            if not auto:
                if self.view.on_off_motor.isChecked() and not exit:
                    estado = "on"
                    texto = "Activar los motores"
                    self.robot_tank.cambiarEstadoDeMotores(True)
                else:
                    estado = "off"
                    texto = "Desctivar los motores"
                    self.robot_tank.cambiarEstadoDeMotores(False)                    
                self.archivo.agregar_accion(accion="action", parametros=estado, tipo="motores" ,texto=texto)
            else:
                if not self.robot_tank.motoresActivados:
                    self.robot_tank.cambiarEstadoDeMotores(True)
                else:
                    self.robot_tank.cambiarEstadoDeMotores(False)
            return True
        except TypeError as e:
            print("Se produjo un error al intentar habilitar motores: {}".format(e))
            return False
            
    def mover(self, direccion, auto=False):
        if self.verificarHabilitacionDeMovimiento():
            if not auto:
                try:
                    if self.startTime > 0:
                        self.endTime = time()
                        self.tiempoTotal = (self.endTime - self.startTime)
                        self.archivo.agregar_accion(accion="duration", parametros=self.tiempoTotal, tipo="movimiento" ,texto=self.texto)
                    if direccion == "adelante":
                        self.robot_tank.mover_adelante()
                        self.texto = "Movimiento hacia adelante"
                    elif direccion == "atras":
                        self.robot_tank.mover_atras()
                        self.texto = "Movimiento hacia atras"
                    elif direccion == "derecha":
                        self.robot_tank.mover_derecha()
                        self.texto = "Girar a la derecha"
                    elif direccion == "izquierda":
                        self.robot_tank.mover_izquierda()
                        self.texto = "Girar a la izquierda"
                    elif direccion == "detener":
                        self.robot_tank.detener_movimiento()
                        self.texto = "Detener el robot"
                    self.startTime = time()
                    return True
                except TypeError as error:
                    info = f"Hubo un error en mover {direccion}, error: {error}"
                    print(info)
                    self.view.add_rlog(info)
                    return False
            else:
                try:
                    if direccion == "adelante":
                        self.robot_tank.mover_adelante()
                    elif direccion == "atras":
                        self.robot_tank.mover_atras()
                    elif direccion == "derecha":
                        self.robot_tank.mover_derecha()
                    elif direccion == "izquierda":
                        self.robot_tank.mover_izquierda()
                    elif direccion == "detener":
                        self.robot_tank.detener_movimiento()
                    return True
                except TypeError as error:
                    info = f"Hubo un error en mover {direccion}, error: {error}"
                    print(info)
                    self.view.add_rlog(info)
                    return False
                
        else:
            print("Falló en la verificación de movimiento, no enviará comandos desde robotController a robot_bt.")
            return False

    def mover_adelante(self):
        return self.mover("adelante")

    def mover_atras(self):
        return self.mover("atras")

    def mover_derecha(self):
        return self.mover("derecha")

    def mover_izquierda(self):
        return self.mover("izquierda")

    def detener_movimiento(self, noGuardar=False):
        return self.mover("detener", auto=noGuardar)

    def verificarHabilitacionDeMovimiento(self):
        if not self.robot_tank.estado_bt:
            info = "La conexión Bluetooth está deshabilitada, habilítela para ejecutar el movimiento deseado."
            self.view.add_rlog(info)
            print(info)
            return False
        elif not self.robot_tank.motoresActivados:
            info = "Los motores están deshabilitados, habilítelos para ejecutar el movimiento deseado."
            self.view.add_rlog(info)
            print(info)
            return False
        else:
            info = "Los motores se encuentran habilitados y comunicados con el robot."
            self.view.add_rlog("Conexión BT: OK   //    Motores: Habilitados")
            print(info)
            return True
        
    def ejecutarXml(self, archivoXml, logFecha):
        try:
            registro = self.archivo.leerXml(archivoXml=archivoXml, fecha=logFecha)
            print(logFecha + '\n')
            print(registro)
            for accion in range(0,len(registro)):
                if registro[accion] == "bluetooth":
                    if registro[accion + 1] == "on":
                        self.view.add_rlog("Ejecutar: {} con estado [{}]".format(registro[accion], registro[accion + 1]))
                        if not self.robot_tank.estado_bt:
                            self.conectarBluetooth(auto=True)
                            sleep(3)
                    elif registro[accion + 1] == "off":
                        self.view.add_rlog("Ejecutar: {} con estado [{}]".format(registro[accion], registro[accion + 1]))
                        self.conectarBluetooth(auto=True) # Verifica estado para desconectar
                        sleep(3)
                    else:
                        print("Error en acción de bluetooth")
                        
                elif registro[accion] == "motores":
                    if registro[accion + 1] == "on":
                        self.view.add_rlog("Ejecutar: {} con estado [{}]".format(registro[accion], registro[accion + 1]))
                        if not self.robot_tank.motoresActivados:
                            self.habilitar_motores(auto=True)
                            sleep(7)
                    elif registro[accion + 1] == "off":
                        self.view.add_rlog("Ejecutar: {} con estado [{}]".format(registro[accion], registro[accion + 1]))
                        self.habilitar_motores(auto=True) # Verifica estado para desconectar
                        sleep(7)
                    else:
                        print("Error en acción de motores")
                        
                elif registro[accion] == "movimiento":
                    if registro[accion - 1] == "Movimiento hacia adelante":
                        tipoMovimiento = "adelante"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "Movimiento hacia atras":
                        tipoMovimiento = "atras"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "Girar a la derecha":
                        tipoMovimiento = "derecha"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "Girar a la izquierda":
                        tipoMovimiento = "izquierda"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "Detener el robot":
                        tipoMovimiento = "detener"
                        duracion = float(registro[accion +1])
                        
                    self.view.add_rlog("Ejecutar: {} con tiempo de [{}] segundos".format(tipoMovimiento, duracion))
                    self.ejecutar_accion(movimiento=tipoMovimiento, tiempo=duracion)
            return True
        except TypeError as e:
            print("Ha ocurrido un error al ejecutar el archivoXML")
            return False

    def ejecutar_accion(self, movimiento, tiempo):
        self.mover(movimiento, True)
        sleep(tiempo)