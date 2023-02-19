from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
from .robot_controller import RobotController
from .xmlrpc_server import XmlRpc_servidor
from PyQt5.QtCore import *

class MainController(QObject):
    def __init__(self, mainView):
        super().__init__()
        self.view = mainView
        self.robotController = RobotController()
        self.view.show()
        # Conexión de señales y slots
        self.view.showEvent = self.show_event
        # self.view.closeEvent = self.close_event

        # Key press event
        self.view.keyPressEvent = self.teclaPresionada
        # Eventos de botones
        self.view.on_off_bt.clicked.connect(self.robotController.conectar_bluetooth)
        # self.view.on_off_bt.clicked.connect(self.alternarTextoBotonBluetooth)

        self.view.on_off_server.clicked.connect(self.iniciar_servidor_xmlrpc)
        
        self.view.on_off_motor.clicked.connect(self.log_habilitarMotores)
        self.view.on_off_motor.clicked.connect(self.robotController.habilitar_motores)
        
        self.view.btn_avanzar.clicked.connect(self.log_moverAdelante)
        self.view.btn_avanzar.clicked.connect(self.robotController.mover_adelante)
        
        self.view.btn_retroceder.clicked.connect(self.robotController.mover_atras)
        self.view.btn_retroceder.clicked.connect(self.log_moverAtras)
        
        self.view.btn_derecha.clicked.connect(self.robotController.mover_derecha)
        self.view.btn_derecha.clicked.connect(self.log_moverDerecha)
        
        self.view.btn_izquierda.clicked.connect(self.robotController.mover_izquierda)
        self.view.btn_izquierda.clicked.connect(self.log_moverIzquierda)
        
        self.view.btn_detener.clicked.connect(self.robotController.detener_movimiento)
        self.view.btn_detener.clicked.connect(self.log_detenerMovimiento)

        # Conectar el evento de cierre de la ventana con el método correspondiente
        self.view.closeEvent = self.on_window_close


    def show_event(self, event):
        print("Showing main window")

    def on_window_close(self, event):
        # Detener el movimiento del robot
        self.robotController.detener_movimiento()
        # Llamar al método original de closeEvent para cerrar la ventana
        event.accept()

    #   Método para
    def iniciar_servidor_xmlrpc(self):
        info = "Se presionó el boton de iniciar/finalizar servidor XML-RPC."
        print(info)
        self.view.add_rlog(info)
        try:
            self.servidor = XmlRpc_servidor(8891)
            self.view.add_rlog("Se logró iniciar el servidor XML-RPC exitosamente en puerto 8891.")
            self.view.add_rlog(" ")
        except TypeError as error:
            self.view.add_rlog("Hubo un error del tipo: {}".format(error))
            self.view.add_rlog(" ")
            print(error)

    #Eventos para controlar los movimientos del robot con le pad númerico del teclado
    def teclaPresionada(self, event):
        if event.key() == Qt.Key_8 and self.teclado_ctrl == True:
            self.view.add_rlog("Se presionó la tecla 8: Mover hacia adelante.")
            self.view.add_rlog(" ")
            self.robotController.mover_adelante()

        elif event.key() == Qt.Key_2 and self.teclado_ctrl == True:
            self.view.add_rlog("Se presionó la tecla 2: Mover hacia atras.")
            self.view.add_rlog(" ")
            self.robotController.mover_atras()

        elif event.key() == Qt.Key_4 and self.teclado_ctrl == True:
            self.view.add_rlog("Se presionó la tecla 4: Girar a la izuierda.")
            self.view.add_rlog(" ")
            self.robotController.mover_izquierda()

        elif event.key() == Qt.Key_6 and self.teclado_ctrl == True:
            self.view.add_rlog("Se presionó la tecla 6: Girar a la derecha.")
            self.view.add_rlog(" ")
            self.robotController.mover_derecha()

        elif event.key() == Qt.Key_5 and self.teclado_ctrl == True:
            self.view.add_rlog("Se presionó la tecla 5: Detener movimiento.")
            self.view.add_rlog(" ")
            self.robotController.detener_movimiento()

    def log_habilitarMotores(self):
        self.view.add_rlog("Se presionó el radioBotón para cambiar estado de motores.")
        self.view.add_rlog(" ")

    def log_moverAdelante(self):
        self.view.add_rlog("Se presionó mover hacia adelante.")
        self.view.add_rlog(" ")

    def log_moverAtras(self):
        self.view.add_rlog("Se presionó mover hacia atras.")
        self.view.add_rlog(" ")

    def log_moverDerecha(self):
        self.view.add_rlog("Se presionó girar a la deerecha.")
        self.view.add_rlog(" ")

    def log_moverIzquierda(self):
        self.view.add_rlog("Se presionó girar a la izquierda.")
        self.view.add_rlog(" ")

    def log_detenerMovimiento(self):
        self.view.add_rlog("Se presionó detener movimiento.")
        self.view.add_rlog(" ")

# if __name__ == '__main__':
#     app = QApplication([])
#     main_controller = MainController()
#     app.exec_()
