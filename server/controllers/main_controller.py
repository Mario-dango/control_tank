from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from views.main_view import MainView
from .robot_controller import RobotController
from .xmlrpc_server import XmlRpc_servidor
from PyQt5.QtCore import *

class MainController(QObject):
    def __init__(self):
        super().__init__()
        self._view = MainView()
        self.servidor = XmlRpc_servidor()
        self._robot_controller = RobotController()
        
        # Conexión de señales y slots
        self._view.showEvent = self.show_event
        self._view.closeEvent = self.close_event
        # Key press event
        self._view.keyPressEvent = self.teclaPresionada
        # Eventos de botones
        self._view.on_off_bt.clicked.connect(self._robot_controller.conectar_bluetooth)
        self._view.on_off_bt.clicked.connect(self.alternarTextoBotonBluetooth)
        
        self._view.on_off_server.clicked.connect(self.iniciar_servidor_xmlrpc)
        self._view.on_off_motor.clicked.connect(self._robot_controller.habilitar_motores)
        self._view.btn_avanzar.clicked.connect(self._robot_controller.mover_adelante)
        self._view.btn_retroceder.clicked.connect(self._robot_controller.mover_atras)
        self._view.btn_derecha.clicked.connect(self._robot_controller.mover_derecha)
        self._view.btn_izquierda.clicked.connect(self._robot_controller.mover_izquierda)
        self._view.btn_detener.clicked.connect(self._robot_controller.detener_movimiento)
        


        # Conectar el evento de cierre de la ventana con el método correspondiente
        self.view.closeEvent = self.on_window_close

        
        # self._view.show()
    
    def show_event(self, event):
        print("Showing main window")
    

    def on_window_close(self, event):
        # Detener el movimiento del robot
        self._robot_controller.detener_movimiento()

        # Llamar al método original de closeEvent para cerrar la ventana
        event.accept()
    
    def alternarTextoBotonBluetooth(self):
        self._view.on_off_bt.setText("")

    def iniciar_servidor_xmlrpc(self):
        # Iniciar servidor
        pass

    #Eventos para controlar los movimientos del robot con le pad númerico del teclado
    def teclaPresionada(self, event):
        if event.key() == Qt.Key_8 and self.teclado_ctrl == True:
            self._robot_controller.mover_adelante()
            
        elif event.key() == Qt.Key_2 and self.teclado_ctrl == True:
            self._robot_controller.mover_atras()
            
        elif event.key() == Qt.Key_4 and self.teclado_ctrl == True:
            self._robot_controller.mover_izquierda()
            
        elif event.key() == Qt.Key_6 and self.teclado_ctrl == True:
            self._robot_controller.mover_derecha()
            
        elif event.key() == Qt.Key_5 and self.teclado_ctrl == True:
            self._robot_controller.detener_movimiento()

if __name__ == '__main__':
    app = QApplication([])
    main_controller = MainController()
    app.exec_()
