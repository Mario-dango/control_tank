#!/usr/bin/python 
# -*- coding: utf-8 -*-

## Recordar ejecutar:
##          sudo rfcomm connect hci 98:D3:31:FC:96:5F
##              (Para conectar con el dispositivo tank)
##          sudo python3 servidor.py
##              (Para poder abrir el programa y poder comunicarse por BT)

import sys
from PyQt5.QtWidgets import QApplication
from controllers.main_controller import MainController
from views.main_view import MainView

if __name__ == "__main__":
    
    #Instancia para iniciar una aplicación
    app = QApplication(sys.argv)
    #Crear un objeto de la clase
    view = MainView() # Instancio primero al objeto de mi ventana principal
    controller = MainController(view)   # Luego instancio mi controlador pasandole mi objeto ventana
    # controller.showMainWindow()
    #Ejecutar la aplicación
    sys.exit(app.exec_())
    