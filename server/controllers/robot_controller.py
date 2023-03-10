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
        self.startTime = 0
        self.endTime = 0
        self.acciones = []

    def conectarBluetooth(self):
        print(self.addressBT)
        try:
            if self.addressBT != "":
                info = "Se presionó el botón de conectar/desconectar Serial Bluetooth."
                print(info)
                self.view.add_rlog(info)
                if not self.robot_tank.estado_bt:
                    self.robot_tank.conectar_bluetooth(self.addressBT)
                    self.startTime = time()
                else:
                    self.robot_tank.estado_bt = False
                    self.robot_tank.bluetooth.disconnect()
        except TypeError as e:
            print("Se produjo un error al intentar conectar al bluetooth: {}".format(e))            
            return False

    def habilitar_motores(self, auto=False): 
        print(self.view.on_off_motor.isChecked()) 
        try:
            if not auto      :
                if self.view.on_off_motor.isChecked():
                    self.robot_tank.cambiarEstadoDeMotores(True)
                else:
                    self.robot_tank.cambiarEstadoDeMotores(False)
            else:
                if not self.robot_tank.motoresActivados:
                    self.robot_tank.cambiarEstadoDeMotores(True)
                else:
                    self.robot_tank.cambiarEstadoDeMotores(False)
            return True
        except TypeError as e:
            print("Se produjo un error al intentar habilitar motores: {}".format(e))
            return False
            
    def mover(self, direccion):
        if self.verificarHabilitacionDeMovimiento():
            try:
                texto = ""
                if direccion == "adelante":
                    self.endTime = time()
                    self.robot_tank.mover_adelante()
                    self.tiempoTotal = (self.endTime - self.startTime)
                    self.startTime = time()
                    texto = "Mover adelante"
                elif direccion == "atras":
                    self.endTime = time()
                    self.robot_tank.mover_atras()
                    self.tiempoTotal = (self.endTime - self.startTime)
                    self.startTime = time()
                    texto = "Mover adelante"
                elif direccion == "derecha":
                    self.endTime = time()
                    self.robot_tank.mover_derecha()
                    self.tiempoTotal = (self.endTime - self.startTime)
                    self.startTime = time()
                    texto = "Mover adelante"
                elif direccion == "izquierda":
                    self.endTime = time()
                    self.robot_tank.mover_izquierda()
                    self.tiempoTotal = (self.endTime - self.startTime)
                    self.startTime = time()
                    texto = "Mover adelante"
                elif direccion == "detener":
                    self.endTime = time()
                    self.robot_tank.detener_movimiento()
                    self.tiempoTotal = (self.endTime - self.startTime)
                    self.startTime = time()
                    texto = "Mover adelante"
                self.archivo.agregar_accion(accion="accion", parametros=direccion, tipo= self.tiempoTotal,texto=texto)
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

    def detener_movimiento(self):
        return self.mover("detener")

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
                            self.conectarBluetooth()
                            sleep(3)
                    elif registro[accion + 1] == "off":
                        self.view.add_rlog("Ejecutar: {} con estado [{}]".format(registro[accion], registro[accion + 1]))
                        self.conectarBluetooth() # Verifica estado para desconectar
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
                    if registro[accion - 1] == "movimiento adelante":
                        tipoMovimiento = "adelante"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "movimiento atras":
                        tipoMovimiento = "atras"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "movimiento derecha":
                        tipoMovimiento = "derecha"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "movimiento izquierda":
                        tipoMovimiento = "izquierda"
                        duracion = float(registro[accion +1])
                    elif registro[accion - 1] == "detenerse":
                        tipoMovimiento = "detener"
                        duracion = float(registro[accion +1])
                        
                    self.view.add_rlog("Ejecutar: {} con tiempo de [{}] segundos".format(tipoMovimiento, duracion))
                    self.ejecutar_accion(movimiento=tipoMovimiento, tiempo=duracion)
            return True
        except TypeError as e:
            print("Ha ocurrido un error al ejecutar el archivoXML")
            return False

    def ejecutar_accion(self, movimiento, tiempo):
        self.mover(movimiento)
        sleep(tiempo)
        # accion = registro['accion']
        # parametros = registro['parametros']
        # tiempo = registro['tiempo']
        # tiempo_actual = datetime.now()
        # tiempo_diferencia = (tiempo - tiempo_actual).total_seconds()
        # if tiempo_diferencia > 0:
        #     sleep(tiempo_diferencia)
        # # Aquí se ejecuta la acción del robot con los parámetros correspondientes
        # print(f"Ejecutando acción '{accion}' con parámetros '{parametros}'")