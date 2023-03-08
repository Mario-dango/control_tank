
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/mainController.hpp"
#pragma once
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"

using namespace std;

//  Constructor 1
MainController::MainController(const char* host, int port)
: controladorXmlRpc(host, port)
{
    this->setIpServidor(controladorXmlRpc.get_host());
    this->setPuerto(controladorXmlRpc.get_puerto());
    CmdVista objetoConsola;
}

//  Constructor simple
// MainController::MainController()
// // : controladorXmlRpc(this->ipServidor, this->puerto)
// // : controladorXmlRpc(this->ipServidor, this->puerto)
// {
//     cout << "Entré al constructor 2" << endl;
//     // this->cmdVista = CmdVista();
//     // this->controladorArchivo = controladorArchivo(nombre);
//     // XmlrpcController xmlrpcController(host, port);
//     CmdVista objetoConsola;
//     ArchivoController *controladorArchivo;
//     XmlrpcController *controladorXmlRpc;

// }

//  Destructor
MainController::~MainController()
{
}

void MainController::run() {
    this->objetoConsola.mostrarMenu();
    const char* archivoXml;
    string cadenaArchivoXml;
    bool resultado;
    string hostSv;
    string puerto;
    // Ejecutar la aplicación
    while (true) {
        int opcion = objetoConsola.leerOpcion();
        switch (opcion) {
            case 0:
                // Cerrar la aplicacion
                return;
            case 1:
                resultado = controladorXmlRpc.activarBluetooth();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 2:
                resultado = controladorXmlRpc.desactivarBluetooth();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 3:
                resultado = controladorXmlRpc.activarMotores();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 4:
                resultado = controladorXmlRpc.desactivarMotores();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 5:
                resultado = controladorXmlRpc.moverAdelante();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 6:
                resultado = controladorXmlRpc.moverAtras();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 7:
                resultado = controladorXmlRpc.moverDerecha();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 8:
                resultado = controladorXmlRpc.moverIzquierda();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 9:
                resultado = controladorXmlRpc.detenerMovimiento();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando                                                                                      .\n");
                }
                break;
            case 10:
                objetoConsola.mostrarMenu();
                break;
            case 11:
                resultado = controladorXmlRpc.solicitarArchivoRegistro();
                if (resultado){
                    objetoConsola.imprimirEnConsola("\nSe envió exitosamente el comando.\n");
                    bool exito = controladorArchivo->guardarArchivoXml("control_tank/client_cmd/resourse/lib/archivos/log.xml", controladorXmlRpc.resultado);
                    if (exito) {
                        objetoConsola.imprimirEnConsola("\nSe guardo el archivo de registro exitosamente.\n");
                    } else {
                        objetoConsola.imprimirEnConsola("\nHubo un error al intentar guardar el archivo XML.\n");
                    }
                } else {
                    objetoConsola.imprimirEnConsola("\nHubo un error al intentar enviar el comando.\n");
                }
                break;
            case 12:
                objetoConsola.mostrarAyuda();
                break;
            case 13:
                objetoConsola.limpiarConsola();
                break;
            case 14:
            // Conectar al servidor
                this->setIpServidor(controladorXmlRpc.get_host());
                this->setPuerto(controladorXmlRpc.get_puerto());
                hostSv = string(this->getIpServidor());
                puerto = to_string(this->getPuerto());
                // cout << hostSv << endl;
                // cout << puerto << endl;
                objetoConsola.imprimirEnConsola("La dirección actual del Servidor XmlRpc es:" + hostSv);
                objetoConsola.imprimirEnConsola("El puerto del Servidor XmlRpc es:" + puerto);
                break;
            case 15:
            // Desconectar del servidorstd::string host = this->getIpServidor();
                int port = this->getPuerto();
                std::string newHost = objetoConsola.cambiarDatos("dirección IP");
                cout << "HOST: " << newHost << endl;
                port = std::stoi(objetoConsola.cambiarDatos("puerto"));
                cout << "PORT: " << port << endl;
                const char* a = newHost.c_str();
                std::string b = std::to_string(port);
                cout << a << endl << b << endl;
                controladorXmlRpc.set_host(a);
                controladorXmlRpc.set_puerto(port);
                objetoConsola.imprimirEnConsola("La dirección nueva del Serv0idor XmlRpc es: " + newHost);
                objetoConsola.imprimirEnConsola("El nuevo puerto del Servidor XmlRpc es: " + std::to_string(port));
                break;
        }
    }
}

int MainController::getPuerto(){
    return this->puerto;
}

const char* MainController::getIpServidor(){
    return this->ipServidor;
}

int MainController::setPuerto(int port){
    // controladorXmlRpc.set_puerto(this->puerto);
    this->puerto = port;
    return this->puerto;
}

const char* MainController::setIpServidor(const char* host){
    // controladorXmlRpc.set_host(this->ipServidor);
    this->ipServidor = host;
    return this->ipServidor;
}
