from PyQt5.QtCore import QObject
from models.robot_bt import Robot
from views.main_view import MainView

class RobotController(QObject):
    def __init__(self, robot):
        super().__init__()
        self.view = MainView()
        self.robot_tank = Robot()
        # self.view.show()
        
    #   Método para 
    def conectar_bluetooth(self):
        info = "Se presionó el boton de conectar/desconectar Serial Bluetooth."
        print(info)
        self.view.add_rlog(info)
        self.robot_tank.conectar_bluetooth()

    #   Método para 
    def iniciar_servidor_xmlrpc(self):
        info = "Se presionó el boton de iniciar/finalizar servidor XML-RPC."
        print(info)
        self.view.add_rlog(info)

    #   Método para 
    def habilitar_motores(self):
        pass

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_adelante(self):
        if self.robot_tank.estado_bt:
            info = "Conectar al robot movil vía bluetooth antes."
            print(info)
            
        pass

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_atras(self):
        pass

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_derecha(self):
        pass

    #   Método para decirle al robot_tank que se mueva y actualice datos
    def mover_izquierda(self):
        print("Se presionó el botón para girar a la izquierda.")
        try:
            if (self.robot_tank.motor_derecho.habilitado):
                self.robot_tank.mover_izquierda()
                self.view.r_log.scrollToBottom()
            else:
                print("Favor de habilitar los motores")
                self.view.r_log.addItem("Los motores están inhabilitados, favor de habilitarlos previamente")

        except TypeError as mensaje:
            print("Error en girar izquierda: {}. Favor de revisar".format(mensaje))
            self.view.r_log.addItem("Error al intentar enviar comando izquierda.")
            self.view.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
            print("Error al intentar enviar comando.")
            print("Revisar estado de la comunicación Bluetooth.")
            self.view.r_log.addItem(" ")
            self.view.r_log.scrollToBottom()
        pass

    #   Método para decirle al robot_tank que se detenga y actualice datos
    def detener_movimiento(self):
        pass

    def verificarConexionBluetooth(self):
        if self.robot_tank.estado_bt == False:
            info = "Conectar al robot movil vía bluetooth antes."
        elif self.robot_tank.estado_bt == True:
            info = "Se verificó conexión exitosa con el robot."
        print(info)
        return

    def verificarEstadoMotores(self):
        if self.robot_tank.motor_derecho.habilitado == False:
            info = "Conectar al robot movil vía bluetooth antes."
        elif self.robot_tank.estado_bt == True:
            info = "Se verificó conexión exitosa con el robot."
        print(info)
        return
            
        
        

    def run(self):
        self.view.show()

