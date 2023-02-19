# from controllers import main_controller
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        # cargar la interfaz de usuario desde el archivo ui generado por Qt Designer
        uic.loadUi('views/ui/panel-control.ui', self)
        self.setWindowTitle("Interfaz de control para Tan-k")
        self.setMinimumSize(1000,600)
        self.setMaximumSize(1001,701)

        # Instancio el objeto mainController para relacionar las conexiones
        # self.mainController = main_controller()

        # setting auto scroll property
        self.r_log.setAutoScroll(True)
        self.r_log.setAutoScrollMargin(20)

        #Colores estado de botoón servidor
        self.btnDesactivo = "background-color: red; border: 1px; padding: 10px"
        self.btnActivo = "background-color: green; border: 1px; padding: 10px"
        #Botones para habilitar o deshabilitar parametros
        self.on_off_bt.setCheckable(True)
        self.on_off_bt.toggle()
        self.on_off_server.setCheckable(True)
        self.on_off_server.toggle()

    #Evento para cuando la ventana se muestra
    def showEvent(self, event):
        self.autor.setText("Autor: Mario Papetti Funes \nInstagram: Mario.spf")
        self.label_2.setText("Registro de acciones realizadas:")
        self.Imagen.setPixmap(QPixmap('resourse/pictures/robot_control.png'))
        # self.Imagen.setPixmap(QPixmap("../resourses/pictures/reobot_control.png"))
        self.t_botones.setText("Botones para controlar el movimiento del robot.")

        # Desabilito todos los botones de movimiento del robot
        self.update_robot_status(False)

        self.r_log.addItem("°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°")
        self.r_log.addItem("Bienvenido a la interfaz para controlar al robot TANK")
        self.r_log.addItem("Para habilitar los botones de control para su movimiento debe de conectar primero el respectivo dispositivo Bluetooth del robot")
        self.r_log.addItem("°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°")
        self.r_log.addItem(" ")



    def set_conectar_robot_bt_text(self, text):
        self.conectar_robot_bt.setText(text)

    def update_robot_status(self, is_connected):
        self.on_off_motor.setEnabled(is_connected)
        self.btn_avanzar.setEnabled(is_connected)
        self.btn_retroceder.setEnabled(is_connected)
        self.btn_izquierda.setEnabled(is_connected)
        self.btn_derecha.setEnabled(is_connected)
        self.btn_detener.setEnabled(is_connected)

    def add_rlog(self, text):
        self.r_log.addItem(text)
        self.r_log.scrollToBottom()


    # #Eventos para conexión/desconexión activación y desactivación de parametros
    # def connect_bluetooth_signal(self):
    #     bt_device = self.bt_list.currentText()
    #     if robot_tank.estado_bt is False:
    #         try:
    #             # self.port_bt = serial.Serial('/dev/rfcomm0',9600)         # Usar en Linux
    #             self.port_bt = serial.Serial("COM8",9600)         # Usar en Windows, para ello revisar donde se conectó el robot en conf de bluetooth
    #             robot_tank.asignar_bt(self.port_bt)

    #             self.r_log.addItem("Se logró la conexión con el dispositivo: " + bt_device)
    #             self.on_off_bt.setText("Bluetooth Conectado!")

    #             # Habilito todos los botones de movimiento del robot
    #             self.update_robot_status(self, True)

    #             self.r_log.addItem(" ")
    #             self.r_log.addItem("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    #             self.r_log.scrollToBottom()
    #             return "Se logró establecer la conexión Bluetooth."
    #         except TypeError as error:
    #             print("ocurrió un error: {}".format(error))
    #             # self.r_log.addItem("Se produjo un error al intentar abrir comunicación por el puerto rfcomm0.")
    #             self.r_log.addItem("Favor de revisar la conexión al dispositivo bluetooth.")
    #             self.on_off_bt.setText("Conectar dispositivo Bluetooth")
    #             self.r_log.addItem(" ")
    #             self.r_log.addItem("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    #             self.r_log.scrollToBottom()
    #             return "No se logró establecer la conexión Bluetooth."

    #     else:
    #         self.detener()
    #         self.en_motors()
    #         robot_tank.estado_bt = False
    #         try:
    #             self.port_bt.close()
    #         except:
    #             print("No se asigno el puerto")
    #         self.on_off_motor.setEnabled(False)
    #         self.btn_avanzar.setEnabled(False)
    #         self.btn_retroceder.setEnabled(False)
    #         self.btn_izquierda.setEnabled(False)
    #         self.btn_derecha.setEnabled(False)
    #         self.btn_detener.setEnabled(False)
    #         self.r_log.addItem("Se desconectó del dispositivo: " + bt_device)
    #         self.on_off_bt.setText("Bluetooth Desconectado")
    #         self.r_log.addItem(" ")
    #         self.r_log.addItem("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    #         self.r_log.scrollToBottom()
    #         return "Se finalizó la conexión Bluetooth."

    # #Evento para habilitar o deshabilitar la función de conexión XmlRpc
    # def en_sv(self):
    #     if self.estado_sv is False:
    #         try:
    #             #Cero al objeto servidor XmlRpc
    #             self.xmlrpc_sv = XmlRpc_servidor(self)
    #             self.estado_sv = True
    #             self.r_log.addItem("Inicializado el servidor")
    #             #self.r_log.addItem("Dirección y puerto del servidor: %s" % str(self.xmlrpc_sv.server_address()))
    #             print("Conectado al servidor")
    #             self.on_off_server.setText("Servidor: Iniciado!")
    #             self.on_off_server.setStyleSheet(self.btnActivo)
    #         except:
    #             print("Error al intentar inicializar servidor")
    #             self.r_log.addItem("Error al intentar inicializar servidor")


    #     else:
    #         try:
    #             self.r_log.addItem("Desconectado del Servidor")
    #             print("Desconectado del Servidor")
    #             self.on_off_server.setText("Servidor: Finalizado!")
    #             #self.r_log.addItem("Dirección y puerto del servidor: %s" % str(self.xmlrpc_sv.server_address()))
    #             self.on_off_server.setStyleSheet(self.btnDesactivo)
    #             self.estado_sv = False
    #             self.xmlrpc_sv.shutdown()
    #             self.xmlrpc_sv = None
    #         except:
    #             print("Error al intentar finalizar servidor")
    #             self.r_log.addItem("Error al intentar finalizar servidor")
    #     self.r_log.addItem("##############################################")
    #     self.r_log.scrollToBottom()


    # ############################################################
    # #Evento para inicializar/finalizar la comunicación Bluetooth
    # def en_motors(self):
    #     try:
    #         if self.estado_mt is False:
    #             self.estado_mt = True
    #             self.teclado_ctrl = True
    #             robot_tank.on_motor(self.port_bt)
    #             self.r_log.addItem("Motores activados.")
    #             self.r_log.addItem("##############################################")
    #             self.r_log.scrollToBottom()
    #             return "Se han habilitado los motores."
    #         elif self.estado_mt is True:
    #             self.estado_mt = False
    #             robot_tank.off_motor(self.port_bt)
    #             self.r_log.addItem("Motores desactivados.")
    #             self.r_log.addItem("##############################################")
    #             self.r_log.scrollToBottom()
    #             return "Se han deshabilitado los motores."
    #     except TypeError as mensaje:
    #             print(f"Error en habilitación de motores: {mensaje}. Favor de revisar")
    #             self.r_log.addItem("Error! Al intentar activas/desactivar motores.")
    #             self.r_log.addItem("##############################################")
    #             self.r_log.scrollToBottom()

    #     ###################################################
    #     #Eventos de botones para control de los movimientos
    # def adelante(self):
    #     self.r_log.addItem("Se presionó el botón para avanzar.")
    #     print("Se presionó el botón para avanzar.")
    #     try:
    #         if (robot_tank.motor_derecho.habilitado):
    #             robot_tank.avanzar(self.port_bt)
    #             self.r_log.scrollToBottom()
    #             return "El tank se mueve hacia Adelante."
    #         else:
    #             print("Favor de habilitar los motores")
    #             self.r_log.addItem("Los motores están inhabilitados, favor de habilitarlos previamente")

    #     except TypeError as mensaje:
    #         print(f"Error en avanzar: {mensaje}. Favor de revisar")
    #         self.r_log.addItem("Error al intentar enviar comando Avanzar.")
    #         self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
    #         print("Error al intentar enviar comando.")
    #         print("Revisar estado de la comunicación Bluetooth.")
    #         self.r_log.addItem(" ")
    #         self.r_log.scrollToBottom()
    #         return "Error al avanzar."

    # def retrocede(self):
    #     self.r_log.addItem("Se presionó el botón para retroceder.")
    #     print("Se presionó el botón para retroceder.")
    #     try:
    #         if (robot_tank.motor_derecho.habilitado):
    #             robot_tank.retroceder(self.port_bt)
    #             self.r_log.scrollToBottom()
    #             return "El tank se mueve hacia Atras."
    #         else:
    #             print("Favor de habilitar los motores")
    #             self.r_log.addItem("Los motores están inhabilitados, favor de habilitarlos previamente")


    #     except TypeError as mensaje:
    #         print(f"Error en retroceder: {mensaje}. Favor de revisar")
    #         self.r_log.addItem("Error al intentar enviar comando retroceder.")
    #         self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
    #         print("Error al intentar enviar comando.")
    #         print("Revisar estado de la comunicación Bluetooth.")
    #         self.r_log.addItem(" ")
    #         self.r_log.scrollToBottom()
    #         return "Error al retroceder."

    # def izquierda(self):
    #     self.r_log.addItem("Se presionó el botón para izquierda.")
    #     print("Se presionó el botón para girar a la izquierda.")
    #     try:
    #         if (robot_tank.motor_derecho.habilitado):
    #             robot_tank.izquierda(self.port_bt)
    #             self.r_log.scrollToBottom()
    #             return "El tank comienza a girar hacia la izquierda."
    #         else:
    #             print("Favor de habilitar los motores")
    #             self.r_log.addItem("Los motores están inhabilitados, favor de habilitarlos previamente")

    #     except TypeError as mensaje:
    #         print(f"Error en girar izquierda: {mensaje}. Favor de revisar")
    #         self.r_log.addItem("Error al intentar enviar comando izquierda.")
    #         self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
    #         print("Error al intentar enviar comando.")
    #         print("Revisar estado de la comunicación Bluetooth.")
    #         self.r_log.addItem(" ")
    #         self.r_log.scrollToBottom()
    #         return "Error al girar a la izquierda."

    # def derecha(self):
    #     self.r_log.addItem("Se presionó el botón para derecha.")
    #     print("Se presionó el botón para girar a la derecha.")
    #     try:
    #         if (robot_tank.motor_derecho.habilitado):
    #             robot_tank.derecha(self.port_bt)
    #             self.r_log.scrollToBottom()
    #             return "El tank comienza a girar hacia la derecha."
    #         else:
    #             print("Favor de habilitar los motores")
    #             self.r_log.addItem("Los motores están inhabilitados, favor de habilitarlos previamente")

    #     except TypeError as mensaje:
    #         print(f"Error en girar derecha: {mensaje}. Favor de revisar")
    #         self.r_log.addItem("Error al intentar enviar comando derecha.")
    #         self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
    #         print("Error al intentar enviar comando.")
    #         print("Revisar estado de la comunicación Bluetooth.")
    #         self.r_log.addItem(" ")
    #         self.r_log.scrollToBottom()
    #         return "Error al girar a la derecha."

    # def detener(self):
    #     self.r_log.addItem("Se presionó el botón para detener.")
    #     print("Se presionó el botón para detener.")

    #     try:
    #         if (robot_tank.motor_derecho.habilitado):
    #             robot_tank.detener(self.port_bt)
    #             self.r_log.scrollToBottom()
    #             return "El tank se ha detenido."
    #         else:
    #             print("Favor de habilitar los motores")
    #             self.r_log.addItem("Los motores están inhabilitados, favor de habilitarlos previamente")

    #     except TypeError as mensaje:
    #         print(f"Error en detener: {mensaje}. Favor de revisar")
    #         self.r_log.addItem("Error al intentar enviar comando detener.")
    #         self.r_log.addItem("Revisar estado de la comunicación Bluetooth.")
    #         print("Error al intentar enviar comando.")
    #         print("Revisar estado de la comunicación Bluetooth.")
    #         self.r_log.addItem(" ")
    #         self.r_log.scrollToBottom()
    #         return "Error al Detenerse."



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    view = MainView()
    view.show()
    app.exec_()
