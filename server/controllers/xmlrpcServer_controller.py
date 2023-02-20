#!/usr/bin/python 
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import socket

class XmlRpc_servidor(object):
    def __init__(self, RobotController, port = 8891):
        self.puerto_usado = port
        self.robotController = RobotController
        self.server = None
        self.estado_sv = False
        while True:
            try:
                #Creacion del servidor indicando el puerto deseado
                self.server = SimpleXMLRPCServer(("localhost", self.puerto_usado), allow_none = True, logRequests = False)
                if self.puerto_usado != port:
                    print("Servidor RPC ubicado en puerto no estándar [%d]" % self.puerto_usado)
                self.estado_sv = True
                break
            except socket.error as e:
                self.estado_sv = False
                if e.errno == 98:
                    self.puerto_usado += 1
                    continue
                else:
                    print("El servidor RPC no puede ser iniciado")
                    raise

        #Se registra cada funcion
        self.server.register_function(self.do_escribir, 'escribir')
        self.server.register_function(self.do_on_off_bt,'buetooth')
        self.server.register_function(self.do_on_off_mt,'motores')
        self.server.register_function(self.do_avanzar,'avanzar')
        self.server.register_function(self.do_retroceder,'retroceder')
        self.server.register_function(self.do_derecha,'derecha')
        self.server.register_function(self.do_izquierda,'izquierda')
        self.server.register_function(self.do_detenerse,'detenerse')
        
    #     #Se lanza el servidor
    #     self.thread = Thread(target = self.run_server)
    #     self.thread.start()
    #     print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))
    # def run_server(self):
    #     if self.estado_sv:
    #         self.server.serve_forever()
        
        self.thread = Thread(target = self.run_server)        

    def run_server(self):
        self.thread.start()
        if self.estado_sv:
            print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))
            self.server.serve_forever()
        #Se lanza el servidor
        
        
    def shutdown(self):
        self.estado_sv = False
        self.server.shutdown()
        self.thread.join()

    def do_escribir(self, texto):
        # Funcion/servicio: mensaje al argumento provisto
        return self.robotController.escribir(texto)
    
    def do_on_off_bt(self):
        return self.robotController.conectar_bluetooth()
        
    def do_on_off_mt(self):
        return self.robotController.habilitar_motores()
        
    def do_avanzar(self):
        return self.robotController.mover_adelante()
    
    def do_retroceder(self):
        return self.robotController.mover_atras()
    
    def do_derecha(self):
        return self.robotController.mover_derecha()
    
    def do_izquierda(self):
        return self.robotController.mover_izquierda()
    
    def do_detenerse(self):
        return self.robotController.detener_movimiento()
    

class XmlRpcServidorOptimizado(object):
    def __init__(self, RobotController, port=8891, max_attempts=10):
        self.puerto_usado = port
        self.robotController = RobotController
        self.server = None
        self.max_attempts = max_attempts
        self.estado_sv = False
        
        # Intentar iniciar el servidor varias veces si hay un error en el puerto
        for i in range(self.max_attempts):
            try:
                self.server = SimpleXMLRPCServer(("localhost", self.puerto_usado), allow_none=True, logRequests=False)
                if self.puerto_usado != port:
                    print("Servidor RPC ubicado en puerto no estándar [%d]" % self.puerto_usado)
                self.estado_sv = True
                break
            except socket.error as e:
                if e.errno == 98:
                    self.puerto_usado += 1
                    continue
                else:
                    print("El servidor RPC no puede ser iniciado")
                    raise

        # Registrar cada función
        self.server.register_function(self.do_escribir, 'escribir')
        self.server.register_function(self.do_on_off_bt, 'buetooth')
        self.server.register_function(self.do_on_off_mt, 'motores')
        self.server.register_function(self.do_avanzar, 'avanzar')
        self.server.register_function(self.do_retroceder, 'retroceder')
        self.server.register_function(self.do_derecha, 'derecha')
        self.server.register_function(self.do_izquierda, 'izquierda')
        self.server.register_function(self.do_detenerse, 'detenerse')
        
        # Iniciar el servidor en un hilo
        self.thread = Thread(target=self.run_server)
        self.thread.start()

    def run_server(self):
        # Verificar si el servidor se inició correctamente
        if self.estado_sv:
            print("Servidor RPC iniciado en el puerto [%s]" % str(self.server.server_address))
            self.server.serve_forever()

    def shutdown(self):
        # Detener el servidor si está en ejecución
        if self.server:
            self.server.shutdown()
        # Esperar a que el hilo termine
        if self.thread:
            self.thread.join()

    def do_escribir(self, texto):
        # Función/servicio: mensaje al argumento provisto
        return self.robotController.escribir(texto)
    
    def do_on_off_bt(self):
        return self.robotController.conectar_bluetooth()
        
    def do_on_off_mt(self):
        return self.robotController.habilitar_motores()
        
    def do_avanzar(self):
        return self.robotController.mover_adelante()
    
    def do_retroceder(self):
        return self.robotController.mover_atras()
    
    def do_derecha(self):
        return self.robotController.mover_derecha()
    
    def do_izquierda(self):
        return self.robotController.mover_izquierda()
    
    def do_detenerse(self):
        return self.robotController.detener_movimiento()

