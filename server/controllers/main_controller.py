from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import *
from .robot_controller import RobotControllerOptimizado
from .xmlrpcServer_controller import XmlRpcServidorOptimizado
from PyQt5.QtCore import *
import serial.tools.list_ports

class MainController(QObject):
    def __init__(self, mainView):
        super().__init__()
        self.view = mainView
        self.robotController = RobotControllerOptimizado(mainView)
        self.estadoServidorXmlrpc = False
        
        

        self.ports = serial.tools.list_ports.comports()
            
        for port, desc, hwid in sorted(self.ports):
            self.view.bt_list.addItem(port)
        
        self.view.show()
        # Conexión de señales y slots
        self.view.showEvent = self.show_event
        # self.view.closeEvent = self.close_event

        self.view.bt_list.currentIndexChanged.connect(self.actualizarPort)
        # Key press event
        self.view.keyPressEvent = self.teclaPresionada
        # Eventos de botones
        self.view.on_off_bt.clicked.connect(self.robotController.conectarBluetooth)
        self.view.on_off_bt.clicked.connect(self.alternarTextoBotonBluetooth)

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
        if self.robotController.robot_tank.estado_bt:                                        
            self.robotController.detener_movimiento()   
            self.robotController.habilitar_motores()
            self.robotController.conectarBluetooth()
                
        if self.estadoServidorXmlrpc:
            self.servidor.shutdown()
            self.estadoServidorXmlrpc = False                                    
        # Llamar al método original de closeEvent para cerrar la ventana
        event.accept()
        exit()

    #   Método para
    def iniciar_servidor_xmlrpc(self):
        info = "Se presionó el boton de iniciar/finalizar servidor XML-RPC."
        print(info)
        # self.view.add_rlog(info)             
        try:
            if not self.estadoServidorXmlrpc:   
                self.servidor = XmlRpcServidorOptimizado(self.robotController, 8891)
                self.estadoServidorXmlrpc = True
                self.view.add_rlog("----------------------------XML-RPC--------------------------------------")
                self.view.add_rlog("Se logró iniciar el servidor XML-RPC exitosamente en puerto 8891.")
            else:
                self.servidor.shutdown()
                self.estadoServidorXmlrpc = False
                self.view.add_rlog("Se logró detener el servidor XML-RPC exitosamente en puerto 8891.")
                self.view.add_rlog("#################################################################")
        except TypeError as error:
            self.view.add_rlog("Hubo un error del tipo: {}".format(error))
            self.view.add_rlog(" ")
            print(error)
                

    #Eventos para controlar los movimientos del robot con le pad númerico del teclado
    def teclaPresionada(self, event):
        self.teclado_ctrl = self.robotController.robot_tank.estado_bt
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

    def actualizarPort(self):
        self.robotController.portBt = self.view.bt_list.currentText()

    def alternarTextoBotonBluetooth(self):
        self.robotController.portBt = self.view.bt_list.currentText()
        print("El puerto tomado es: {}".format(self.robotController.portBt))
        # print("Impresión de puerto {} en el evento showWindow en mainController".format(self.robotController.portBt))
        if self.robotController.robot_tank.estado_bt:
            self.view.on_off_bt.setText("CONECTADO!")
            print(self.robotController.portBt)
        else:
            self.view.on_off_bt.setText("Conectar dispositivo Bluetooth")
            self.robotController.portBt = self.view.bt_list.currentText()
            
        self.view.add_rlog("Se presionó el botón para conectar el bluetooth por el puerto {}.".format(self.robotController.portBt))
        self.view.add_rlog(" ")

    def log_habilitarMotores(self):
        self.view.add_rlog("Se presionó el radioBotón para cambiar estado de motores.")
        if self.view.on_off_motor.isChecked():
            self.view.add_rlog("Se procederá a Activar los motores del Robot.")
        else:    
            self.view.add_rlog("Se procederá a Desactivar los motores del Robot.")
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
