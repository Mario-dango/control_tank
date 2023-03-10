#define PY_SSIZE_T_CLEAN
from PyQt5.QtWidgets import *
from .robot_controller import RobotControllerOptimizado
from .xmlrpcServer_controller import XmlRpcServidorOptimizado
from .xmlrpcServer_controller import ArchivoController
from PyQt5.QtCore import *
import bluetooth

class MainController(QObject):
    def __init__(self, mainView):
        super().__init__()
        self.view = mainView
        self.robotController = RobotControllerOptimizado(mainView)
        self.controladorDeArchivos = ArchivoController()
        self.estadoServidorXmlrpc = False
        self.devices = bluetooth.discover_devices()
        self.archivo = None
        self.archivoXml = None
        self.view.update_botones_status(False)
        self.opcionesRegistro = []
        self.flagRunXml = False
        
        try:
            for device in self.devices:
                print(device)
                print(type(device))
                name = bluetooth.lookup_name(device)
                self.view.bt_list.addItem(f'{name} ({device})')
        except Exception as e:
            print("Ha ocurrido un Error: ", e)

        
        self.view.show()
        # self.view.closeEvent = self.close_event

        self.view.bt_list.currentIndexChanged.connect(self.actualizarPort)
        # Key press event
        self.view.keyPressEvent = self.teclaPresionada
        # Eventos de botones
        self.view.on_off_bt.clicked.connect(self.alternarTextoBotonBluetooth)
        # self.view.on_off_bt.clicked.connect(self.robotController.conectarBluetooth)

        self.view.on_off_server.clicked.connect(self.iniciar_servidor_xmlrpc)
        
        self.view.on_off_motor.clicked.connect(self.log_habilitarMotores)
        self.view.on_off_motor.clicked.connect(self.robotController.habilitar_motores)
        
        self.view.btn_avanzar.clicked.connect(self.robotController.mover_adelante)
        self.view.btn_avanzar.clicked.connect(self.log_moverAdelante)
        
        self.view.btn_retroceder.clicked.connect(self.robotController.mover_atras)
        self.view.btn_retroceder.clicked.connect(self.log_moverAtras)
        
        self.view.btn_derecha.clicked.connect(self.robotController.mover_derecha)
        self.view.btn_derecha.clicked.connect(self.log_moverDerecha)
        
        self.view.btn_izquierda.clicked.connect(self.robotController.mover_izquierda)
        self.view.btn_izquierda.clicked.connect(self.log_moverIzquierda)
        
        self.view.btn_detener.clicked.connect(self.robotController.detener_movimiento)
        self.view.btn_detener.clicked.connect(self.log_detenerMovimiento)
        #leerXml
        # self.view.btn_runXml.clicked.connect()# cómo puta hacer para enviarle a que ejecute los parámetros vieja
        self.view.btn_runXml.clicked.connect(self.log_runXml)
        self.view.btn_runXml.setText("Ejecutar")
        
        self.view.btn_logXml.clicked.connect(self.imprimirXml)
        self.view.lte_Xml.textChanged.connect(self.miniConsola)
        # self.view.btn_logXml.clicked.connect(self.log_detenerMovimiento)

        # Conectar el evento de cierre de la ventana con el método correspondiente
        self.view.closeEvent = self.on_window_close

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
                self.view.update_botones_status(False)
                self.teclado_ctrl = False
                self.view.add_rlog("----------------------------XML-RPC--------------------------------------")
                self.view.add_rlog("Se logró iniciar el servidor XML-RPC exitosamente con dirección: {} en puerto {}.".format(self.servidor.host_apuntado, self.servidor.puerto_usado))
            else:
                self.servidor.shutdown()
                self.estadoServidorXmlrpc = False
                if self.robotController.robot_tank.estado_bt:
                    self.view.update_botones_status(True)
                    self.teclado_ctrl = True
                self.view.add_rlog("Se logró detener el servidor XML-RPC exitosamente con dirección: {} en puerto {}.".format(self.servidor.host_apuntado, self.servidor.puerto_usado))
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
        self.robotController.addressBT = self.view.bt_list.currentText()
        print("El puerto tomado es: {}".format(self.robotController.addressBT))
        self.robotController.conectarBluetooth()
        if self.robotController.robot_tank.estado_bt:
            self.view.on_off_bt.setText("CONECTADO!")
            self.view.update_botones_status(True)
            print(self.robotController.addressBT)
            self.robotController.conectarBluetooth
        else:
            self.view.update_botones_status(False)
            self.view.on_off_bt.setText("Conectar dispositivo Bluetooth")
            print(self.robotController.addressBT)
            self.robotController.conectarBluetooth
            self.robotController.addressBT = self.view.bt_list.currentText()
            
        self.view.add_rlog("Se presionó el botón para conectar el bluetooth por el puerto {}.".format(self.robotController.addressBT))
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
        
    def log_runXml(self):    
        if self.flagRunXml is not True:
            self.view.add_rlog("\nSE PROCEDE A EJECUTAR LA TAREA XML")
            self.view.update_botones_status(False)
            self.view.btn_runXml.setText("Ejecutar XML")
            self.archivoXml = self.archivo
            self.opcionesRegistro = self.controladorDeArchivos.registros(self.archivoXml)
            if len(self.opcionesRegistro) == 1:
                self.view.add_rlog(self.opcionesRegistro[0])
                self.view.update_botones_status(True)
                self.view.lte_Xml.clear()
                return
            else:
                self.view.add_rlog("Seleccione el Número correspondiente al registro para ejecutar")
                for texto in self.opcionesRegistro:
                    self.view.add_rlog(texto)
                self.archivoXml = self.archivo
                self.flagRunXml = True
                self.view.lte_Xml.clear()
                    
        elif self.flagRunXml is not False:
            opcion = int(self.archivo)
            opcionFecha = self.opcionesRegistro[opcion].split("\t")
            logFecha = opcionFecha[0].split(" ")[-1].strip()
            self.view.add_rlog("\nLOG_" + logFecha)
            self.flagRunXml = False            
            exito = self.robotController.ejecutarXml(self.archivoXml, logFecha)
            self.view.lte_Xml.clear()
            if exito:
                self.view.add_rlog("\nFINALIZÓ LA EJECUCIÓN DE LA TAREA XML")
            else:
                self.view.add_rlog("\nSE PROCEDE A EJECUTAR LA TAREA XML")
            self.view.btn_runXml.setText("Ejecutar")
            
        
    def miniConsola(self, texto):
        self.archivo = texto
        
    def imprimirXml(self):
        cadenaArchivo = self.controladorDeArchivos.leerXml(self.archivo)
        if len(cadenaArchivo) == 1:
            self.view.add_rlog(cadenaArchivo[0])
        else:
            for texto in cadenaArchivo:
                self.view.add_rlog(texto)
# if __name__ == '__main__':
#     app = QApplication([])
#     main_controller = MainController()
#     app.exec_()
