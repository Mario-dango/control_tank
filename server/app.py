#!/usr/bin/python 
#define PY_SSIZE_T_CLEAN
# -*- coding: utf-8 -*-

## Recordar ejecutar:
##          sudo rfcomm connect hci 98:D3:31:FC:96:5F
## acá el HC-05 20:16:04:18:35:40
##              (Para conectar con el dispositivo tank)
##          sudo python3 servidor.py
##              (Para poder abrir el programa y poder comunicarse por BT)

import sys
from PyQt5.QtWidgets import QApplication
from controllers.main_controller import MainController
from views.main_view import MainView

# /home/bawy/Plantillas/git_poo/control_tank/server/archivos/log.xml
#   Ruta relativa si se ejecuta desde control_tank -> control_tank/server/archivos/log.xml
import sys
if sys.version_info < (3, 0):
    raise ValueError("Se requiere Python 3.x")

if __name__ == "__main__":
    
    #Instancia para iniciar una aplicación
    app = QApplication(sys.argv)
    #Crear un objeto de la clase
    view = MainView() # Instancio primero al objeto de mi ventana principal
    controller = MainController(view)   # Luego instancio mi controlador pasandole mi objeto ventana
    # controller.showMainWindow()
    #Ejecutar la aplicación
    sys.exit(app.exec_())
    
    
