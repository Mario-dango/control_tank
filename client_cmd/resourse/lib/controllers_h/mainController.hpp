#ifndef MAINCONTROLLER_HPP
#define MAINCONTROLLER_HPP
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/archivoController.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/views_h/cmdView.hpp"

class MainController {
public:
    //  Definir constrictor
    MainController(const char* host, int port);
    // MainController(const char* nombre, const char* host, int port);
    ~MainController();
    //  Inicia el controlador principal del programa.
    void run();
    
    //  Métodos setters y getters.
    int setPuerto(int port);
    const char* setIpServidor(const char* host);
    int getPuerto();
    const char* getIpServidor();
    //  Composición Objeto de visualización de datos.
    CmdVista objetoConsola;
    //  Composición Objeto controlador de archivos.
    ArchivoController *controladorArchivo;
    //  Composición Objeto controlador de conexión XmlRpc cliente
    XmlrpcController controladorXmlRpc;

private:
    //  Dirección del servidor XmlRpc.
    const char* ipServidor;
    //  Puerto del servidor XmlRpc.
    int puerto;
};

#endif // MAINCONTROLLER_HPP
