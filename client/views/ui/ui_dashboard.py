# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'x:\UNCuyo\Por Cursar\POO\Poo_libre\client\views\ui\dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1035, 617)
        MainWindow.setStyleSheet("background-color: rgb(97, 53, 131);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_arriba = QtWidgets.QFrame(self.centralwidget)
        self.frame_arriba.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_arriba.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_arriba.setObjectName("frame_arriba")
        self.autor = QtWidgets.QLabel(self.frame_arriba)
        self.autor.setGeometry(QtCore.QRect(20, 210, 691, 51))
        self.autor.setObjectName("autor")
        self.layoutWidget = QtWidgets.QWidget(self.frame_arriba)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 20, 601, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_retroceder = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_retroceder.setObjectName("btn_retroceder")
        self.gridLayout.addWidget(self.btn_retroceder, 4, 1, 1, 1)
        self.btn_detener = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_detener.setObjectName("btn_detener")
        self.gridLayout.addWidget(self.btn_detener, 3, 1, 1, 1)
        self.on_off_bt = QtWidgets.QPushButton(self.layoutWidget)
        self.on_off_bt.setObjectName("on_off_bt")
        self.gridLayout.addWidget(self.on_off_bt, 1, 3, 1, 1)
        self.btn_avanzar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_avanzar.setAutoDefault(True)
        self.btn_avanzar.setObjectName("btn_avanzar")
        self.gridLayout.addWidget(self.btn_avanzar, 2, 1, 1, 1)
        self.btn_izquierda = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_izquierda.setObjectName("btn_izquierda")
        self.gridLayout.addWidget(self.btn_izquierda, 3, 0, 1, 1)
        self.t_botones = QtWidgets.QLabel(self.layoutWidget)
        self.t_botones.setObjectName("t_botones")
        self.gridLayout.addWidget(self.t_botones, 1, 0, 1, 1)
        self.bt_list = QtWidgets.QComboBox(self.layoutWidget)
        self.bt_list.setObjectName("bt_list")
        self.bt_list.addItem("")
        self.bt_list.addItem("")
        self.gridLayout.addWidget(self.bt_list, 0, 3, 1, 1)
        self.on_off_motor = QtWidgets.QRadioButton(self.layoutWidget)
        self.on_off_motor.setObjectName("on_off_motor")
        self.gridLayout.addWidget(self.on_off_motor, 0, 0, 1, 3)
        self.btn_derecha = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_derecha.setObjectName("btn_derecha")
        self.gridLayout.addWidget(self.btn_derecha, 3, 2, 1, 1)
        self.on_off_server = QtWidgets.QPushButton(self.layoutWidget)
        self.on_off_server.setObjectName("on_off_server")
        self.gridLayout.addWidget(self.on_off_server, 2, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 3, 1, 1)
        self.Imagen_2 = QtWidgets.QLabel(self.frame_arriba)
        self.Imagen_2.setGeometry(QtCore.QRect(10, 10, 350, 200))
        self.Imagen_2.setMinimumSize(QtCore.QSize(350, 200))
        self.Imagen_2.setMaximumSize(QtCore.QSize(350, 200))
        self.Imagen_2.setStyleSheet("border: 5px solid black;")
        self.Imagen_2.setText("")
        self.Imagen_2.setPixmap(QtGui.QPixmap("x:\\UNCuyo\\Por Cursar\\POO\\Poo_libre\\client\\views\\ui\\../../../../on_linux/poo_libre/imagenes/tank000.png"))
        self.Imagen_2.setScaledContents(True)
        self.Imagen_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Imagen_2.setObjectName("Imagen_2")
        self.verticalLayout.addWidget(self.frame_arriba)
        self.frame_abajo = QtWidgets.QFrame(self.centralwidget)
        self.frame_abajo.setAutoFillBackground(False)
        self.frame_abajo.setStyleSheet("background-color: rgb(28, 113, 216);")
        self.frame_abajo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_abajo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_abajo.setObjectName("frame_abajo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_abajo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 14, 971, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.r_log = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.r_log.setObjectName("r_log")
        self.verticalLayout_2.addWidget(self.r_log)
        self.verticalLayout.addWidget(self.frame_abajo)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.autor.setText(_translate("MainWindow", "TextLabel"))
        self.btn_retroceder.setText(_translate("MainWindow", "Retroceder"))
        self.btn_detener.setText(_translate("MainWindow", "Detener"))
        self.on_off_bt.setText(_translate("MainWindow", "Conectar dispositivo Bluetooth"))
        self.btn_avanzar.setText(_translate("MainWindow", "Avanzar"))
        self.btn_izquierda.setText(_translate("MainWindow", "Izquierda"))
        self.t_botones.setText(_translate("MainWindow", "TextLabel"))
        self.bt_list.setItemText(0, _translate("MainWindow", "98:D3:31:FC:96:5F - HC-06"))
        self.bt_list.setItemText(1, _translate("MainWindow", "94:17:00:DD:74:5F - Bawy~"))
        self.on_off_motor.setText(_translate("MainWindow", "Activar / Desactivar Motores"))
        self.btn_derecha.setText(_translate("MainWindow", "Derecha"))
        self.on_off_server.setText(_translate("MainWindow", "Botón Servidor"))
        self.pushButton.setText(_translate("MainWindow", "Cerrar sesión"))
        self.label.setText(_translate("MainWindow", "Logueado cómo: "))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
