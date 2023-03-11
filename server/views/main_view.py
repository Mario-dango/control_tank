#define PY_SSIZE_T_CLEAN
#!/usr/bin/python 
# -*- coding: utf-8 -*-
# # from controllers import main_controller
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        # cargar la interfaz de usuario desde el archivo ui generado por Qt Designer
        uic.loadUi('views/ui/dashboard.ui', self)
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
        # Desabilito todos los botones de movimiento del robot
        self.update_botones_status(True)
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


        self.r_log.addItem("°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°")
        self.r_log.addItem("Bienvenido a la interfaz para controlar al robot TANK")
        self.r_log.addItem("Para habilitar los botones de control para su movimiento debe de conectar primero el respectivo dispositivo Bluetooth del robot")
        self.r_log.addItem("El archivo de registro se encuentra en la carpeta de archivos en el proyecto:")
        self.r_log.addItem("archivos/log.xml")
        self.r_log.addItem("°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°°°\_/°°")
        self.r_log.addItem(" ")

    def set_conectar_robot_bt_text(self, text):
        self.conectar_robot_bt.setText(text)

    def update_botones_status(self, is_connected):
        self.on_off_motor.setEnabled(is_connected)
        self.btn_avanzar.setEnabled(is_connected)
        self.btn_retroceder.setEnabled(is_connected)
        self.btn_izquierda.setEnabled(is_connected)
        self.btn_derecha.setEnabled(is_connected)
        self.btn_detener.setEnabled(is_connected)

    def add_rlog(self, text):
        self.r_log.addItem(text)
        self.r_log.scrollToBottom()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication([])
#     view = MainView()
#     view.show()
#     app.exec_()
