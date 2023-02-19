from PyQt5.QtCore import QObject
from models.robot_bt import Robot
from views.main_view import MainView

class RobotController(QObject):
    def __init__(self):
        super().__init__()
        self.view = MainView()
        self.robot_tank = Robot()
        
    #   Método para 
    def conectar_bluetooth(self):
        info = "Se presionó el boton de conectar/desconectar Serial Bluetooth."
        print(info)
        self.view.add_rlog(info)
        self.robot_tank.conectar_bluetooth()

    #   Método para 
    def habilitar_motores(self):
        if self.robot_tank.motoresActivados:
            self.robot_tank.cambiarEstadoDeMotores(False)
        else:
            self.robot_tank.cambiarEstadoDeMotores(True)

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_adelante(self):
        if self.verificarHabilitacionDeMovimiento():
            try:
                self.robot_tank.mover_adelante()
            except TypeError as error:
                info = "Hubo un error en mover hacia delante, error: {}".format(error)
                print(info)
                self.view.add_rlog(info)
        else: pass

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_atras(self):
        if self.verificarHabilitacionDeMovimiento():
            try:
                self.robot_tank.mover_atras()
            except TypeError as error:
                info = "Hubo un error en mover hacia atras, error: {}".format(error)
                print(info)
                self.view.add_rlog(info)
        else: pass

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_derecha(self):
        if self.verificarHabilitacionDeMovimiento():
            try:
                self.robot_tank.mover_derecha()
            except TypeError as error:
                info = "Hubo un error en mover a la derecha, error: {}".format(error)
                print(info)
                self.view.add_rlog(info)
        else: pass        

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_izquierda(self):
        if self.verificarHabilitacionDeMovimiento():
            try:
                self.robot_tank.mover_izquierda()
            except TypeError as error:
                info = "Hubo un error en mover a la izquierda, error: {}".format(error)
                print(info)
                self.view.add_rlog(info)
        else: pass

    #   Método para decirle al robot_tank que se detenga y actualice datos
    def detener_movimiento(self):
        if self.verificarHabilitacionDeMovimiento():
            try:
                self.robot_tank.detener_movimiento()
            except TypeError as error:
                info = "Hubo un error en detener movimiento, error: {}".format(error)
                print(info)
                self.view.add_rlog(info)
        else: pass

    def verificarConexionBluetooth(self):
        if self.robot_tank.estado_bt == False:
            info = "Conectar al robot movil vía bluetooth antes."
        elif self.robot_tank.estado_bt == True:
            info = "Se verificó conexión exitosa con el robot."
        print(info)
        self.view.add_rlog(info)
        return
    
    def verificarHabilitacionDeMovimiento(self):
        if self.robot_tank.estado_bt:
            if self.robot_tank.motoresActivados:
                print("Los motores se encuentran habilitados y comunicados con el robot.")
                self.view.add_rlog("Conexión BT: OK   //    Motores: Habilitados")
                return True
            else:
                print("Los motores estan deshabilitados, habilitelos para ejecutar el movimiento deseado.")
                self.view.add_rlog("Habilitar los motores para poder ejecutar movimientos.")                
                return False
        else:
            print("La conexión Bluetooth está deshabilitada, habilitela para ejecutar el movimiento deseado.")
            self.view.add_rlog("Revisar estado de la comunicación Bluetooth.")
            return False
            
        