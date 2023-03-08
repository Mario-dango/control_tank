#define PY_SSIZE_T_CLEAN
#!/usr/bin/python
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.server
from threading import Thread
from controllers.archivo_controller import ArchivoController
import os
import signal
import socket

class XmlRpcServidorOptimizado(object):
    def __init__(self, RobotController, port=8891, max_attempts=10):
        self.puerto_usado = port
        self.host_apuntado = "127.0.0.1"
        self.controladorArchivos = ArchivoController
        self.robotController = RobotController
        self.server = None
        self.max_attempts = max_attempts
        self.estado_sv = False

        # Intentar iniciar el servidor varias veces si hay un error en el puerto
        for i in range(self.max_attempts):
            try:
                self.server = SimpleXMLRPCServer((self.host_apuntado, self.puerto_usado), allow_none=True, logRequests=False)
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
        # self.server.register_function(self.do_escribir, 'escribir')
        self.server.register_function(self.do_on_off_bt, 'bluetooth')
        self.server.register_function(self.do_on_off_mt, 'motores')
        self.server.register_function(self.do_avanzar, 'avanzar')
        self.server.register_function(self.do_retroceder, 'retroceder')
        self.server.register_function(self.do_derecha, 'derecha')
        self.server.register_function(self.do_izquierda, 'izquierda')
        self.server.register_function(self.do_detenerse, 'detenerse')

        self.server.register_function(self.do_solicitarXml, 'solicitarXml')

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
            # Obtener el ID del proceso del servidor
            pid = self.server.socket.getsockname()[1]
            # Matar el proceso del servidor
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError as error:
                print("Ha ocurrido un error al intentar matar el servidor (PID={}): {}".format(pid, error))
            
        # Esperar a que el hilo termine
        if self.thread:
            self.thread.join()

    def do_on_off_bt(self):
        return self.robotController.conectarBluetooth()

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

    def do_solicitarXml(self):
        return self.controladorArchivos.solicitarXml()

    def do_enviarXml(self):
        binaryXml = self.controladorArchivos.leerBinaryXml("control_tank/server/archivos/log.xml")
        return xmlrpc.client.Binary(binaryXml.encode())
    

