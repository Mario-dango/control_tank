from PyQt5.QtCore import QObject
from models.robot_bt import Robot
from views.main_view import MainView

class RobotController(QObject):
    def __init__(self):
        super().__init__()
        self.view = MainView()
        self.robot_tank = Robot()
        self.portBt = self.view.bt_list.currentText()
        
    #   Método para 
    def conectarBluetooth(self):
        if self.portBt != "":
            info = "Se presionó el boton de conectar/desconectar Serial Bluetooth."
            print(info)
            self.view.add_rlog(info)
            if self.robot_tank.estado_bt:      
                self.robot_tank.conectar_bluetooth(self.portBt)  
                # Desabilito todos los botones de movimiento del robot
                self.view.update_robot_status(True)    
            else:
                self.robot_tank.conectar_bluetooth(self.portBt)
            

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
            
 
class RobotControllerOptimizado(QObject):
    def __init__(self):
        super().__init__()
        self.view = MainView()
        self.robot_tank = Robot()
        self.portBt = self.view.bt_list.currentText()
        # self.teclado_ctrl = False       #   Habilita control de teclas en interfaz provista por conexión exitosa
        # self.conexionBluetooth = False 

    def conectarBluetooth(self):
        if self.portBt:
            info = "Se presionó el botón de conectar/desconectar Serial Bluetooth."
            print(info)
            self.view.add_rlog(info)
            self.robot_tank.conectar_bluetooth(self.portBt) if self.robot_tank.estado_bt else self.robot_tank.conectar_bluetooth(self.portBt)

    def habilitar_motores(self):
        self.robot_tank.cambiarEstadoDeMotores(not self.robot_tank.motoresActivados)

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
            # self.teclado_ctrl = True
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


       