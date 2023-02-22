from PyQt5.QtCore import QObject
from models.robot_bt import Robot
from views.main_view import MainView
class RobotControllerOptimizado(QObject):
    def __init__(self, mainView):
        super().__init__()
        self.view = mainView
        self.robot_tank = Robot()
        self.portBt = self.view.bt_list.currentText()
        # self.teclado_ctrl = False       #   Habilita control de teclas en interfaz provista por conexión exitosa
        # self.conexionBluetooth = False 

    def conectarBluetooth(self):
        if self.portBt:
            info = "Se presionó el botón de conectar/desconectar Serial Bluetooth."
            print(info)
            self.view.add_rlog(info)
            if not self.robot_tank.estado_bt:
                self.robot_tank.conectar_bluetooth(self.portBt)
            else:
                self.robot_tank.bluetooth.disconnect()


    def habilitar_motores(self): 
        print(self.view.on_off_motor.isChecked())       
        if self.view.on_off_motor.isChecked():
            self.robot_tank.cambiarEstadoDeMotores(True)
        else:
            self.robot_tank.cambiarEstadoDeMotores(False)
            



    def mover(self, direccion):
        if self.verificarHabilitacionDeMovimiento():
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
            except TypeError as error:
                info = f"Hubo un error en mover {direccion}, error: {error}"
                print(info)
                self.view.add_rlog(info)
        else:
            print("Falló en la verificación de movimiento, no enviará comandos desde robotController a robot_bt.")

    def mover_adelante(self):
        self.mover("adelante")

    def mover_atras(self):
        self.mover("atras")

    def mover_derecha(self):
        self.mover("derecha")

    def mover_izquierda(self):
        self.mover("izquierda")

    def detener_movimiento(self):
        self.mover("detener")

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


       