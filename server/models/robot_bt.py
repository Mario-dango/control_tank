#!/usr/bin/python 
# -*- coding: utf-8 -*-

from .PCB import PCB_mother
from .motor import Motor
from .sensor_temperatura import Sensor_temp
from .bluetooth_model import BlueRobot

## Será el encargado de generar la conexión bluetooth !!
        
class Robot:

    def __init__(
                self, 
                voltaje_motor = "12v",
                direccion = "ninguna",
                velocidad = 0,
                cantidad_celdas = 6,
                estado_bluetooth = False
                ):
        # Usar en Windows, para ello revisar donde se conectó el robot en conf de bluetooth
        
        self.voltaje_motor = voltaje_motor
        self.direccion = direccion
        self.velocidad = velocidad
        self.estado_bt = estado_bluetooth
        self.cantidad_celdas = cantidad_celdas
        self.motoresActivados = False
        self.pcb = PCB_mother("v1.0", "2022-02-15 rev:4.2", "Mario Papetti")
        self.motor_izquierdo = Motor("Nema17", "Paso a paso", "Detenido", False)
        self.motor_derecho = Motor("Nema17", "Paso a paso", "Detenido", False)
        self.sensor_baterias = Sensor_temp(0, 0)
        self.bluetooth = BlueRobot("COM11", 9600)
    
    
    def conectar_bluetooth(self, puerto):      
        # Código para conectar el robot por Bluetooth
        try:
            if self.estado_bt == False:
                self.bluetooth.changePort(puerto)
                if self.bluetooth.connect():
                    self.estado_bt = True
                else: pass
            elif self.estado_bt == True:
                if self.bluetooth.disconnect():
                    self.bluetooth.changePort(puerto)
                    self.estado_bt = False
            else: print("error re raro che.")
        except TypeError as error:
            self.estado_bt = False
            print("Hubo un problema al intentar conectar con el robot.")
            print("El error es: {}".format(error))
      
    #   Método para cambiar el estado del objeto robot_tank
    def cambiar_estado_bt(self):
        self.estado_bt = not self.estado_bt
        
    def habilitar_motores(self):        # Código para habilitar los motores del robot
        dato = 'A'       # Comando que habilita ambos motores
        self.actualizar_robot(dato, "Ninguna, detenido.", 0, "Detenido.", "Detenido.")

    def deshabilitar_motores(self):        # Código para deshabilitar los motores del robot
        dato = 'B'       # Comando que deshabilita ambos motores
        self.actualizar_robot(dato, "Ninguna, detenido.", 0, "Detenido.", "Detenido.")
        
    def mover_adelante(self):      
        dato = '8'
        self.actualizar_robot(dato, "Avanza hacia adelante.", 3, "Giro antihorario.", "Giro horario.")
    
    def mover_atras(self):
        dato = '2'
        self.actualizar_robot(dato, "NAvanza hacia atraz.", 3, "Giro horario.", "Giro antihorario.")
            
    def mover_derecha(self):
        dato = '6'
        self.actualizar_robot(dato, "Gira a la derecha.", 0, "Giro antihorario.", "Giro antihorario.")
    
    def mover_izquierda(self):
        dato = '4'
        self.actualizar_robot(dato, "Gira a la izquierda.", 3, "Giro horario.", "Giro horario.")
    
    def detener_movimiento(self):
        dato = '0'       # Código para detener el movimiento del robot
        self.actualizar_robot(dato, "Ninguna, detenido.", 0, "Detenido.", "Detenido.")
    
    def actualizar_robot(self, comando, newDireccion, newVelocidad, newEstadoMotorIzquierdo, newEstadoMotorDerecho):
        try:
            # self.bluetooth.serial.write(comando)
            self.bluetooth.send(comando)
            if self.motoresActivados:
                self.direccion = newDireccion
                self.velocidad = newVelocidad
                self.motor_derecho.cambiar_estado(newEstadoMotorDerecho)
                self.motor_izquierdo.cambiar_estado(newEstadoMotorIzquierdo)
        except TypeError as error:
            print("Hubo un error en la comunicación.")
            print("El error es: {}".format(error))
    
    def cambiarEstadoDeMotores(self, estado):
        if self.motoresActivados == False and estado:
            self.habilitar_motores()
            # self.motoresActivados = not self.motoresActivados
            # print(estado)
        elif self.motoresActivados == True and not estado:
            self.deshabilitar_motores()
        # else:
        #     self.deshabilitar_motores()        
        self.motor_derecho.cambiar_habilitacion(estado)
        self.motor_izquierdo.cambiar_habilitacion(estado)
        self.motoresActivados = estado
        



