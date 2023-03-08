#ifndef XMLRPC_CONTROLLER_HPP
#define XMLRPC_CONTROLLER_HPP

#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpc/XmlRpcClient.h"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpc/XmlRpc.h"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/views_h/cmdView.hpp"



class XmlrpcController : XmlRpc::XmlRpcClient {
  public:
    //  Defino el constructor.
    XmlrpcController(const char* host, int port);
    //  Defino el destrructor.
    ~XmlrpcController();

    // bool connectToServer();
    // void disconnectFromServer();

    // std::string sendRequest(const std::string& methodName, XmlRpc::XmlRpcValue& params);
    bool enviar(const int caso);
    //  Métodos para la interacciones del robot móvil
    bool activarBluetooth();
    bool desactivarBluetooth();
    bool activarMotores();
    bool desactivarMotores();
    bool moverAdelante();
    bool moverAtras();
    bool moverDerecha();
    bool moverIzquierda();
    bool detenerMovimiento();
    //  Métodos referentes al manejo de archivos XML.
///////////////////// Definir cómo pasar la ruta del archivo.xml
    bool solicitarArchivoRegistro();
    // Métodos setters y getters.
    int set_puerto(int puerto);
    const char* set_host(const char* servidorHost);
    int get_puerto();
    const char* get_host();
    //  Valores tipo XmlRpcValue
    XmlRpc::XmlRpcValue parametro, resultado, data;

  private:
    // XmlRpc::XmlRpcClient _client;
    //  Objeto consola para la muestra de información.
    CmdVista consola;
    // XmlRpc::XmlRpcClient cliente;
    //  Dirección IP del servidor XmlRpc.
    const char* host;
    //  Puerto de conexión al servidor XmlRpc.
    int port;    
};

#endif
