#ifndef XMLRPC_CONTROLLER_HPP
#define XMLRPC_CONTROLLER_HPP

#include "../client_cmd/resourse/lib/controllers_h/xmlrpc/XmlRpcClient.h"
#include "../client_cmd/resourse/lib/controllers_h/xmlrpc/XmlRpc.h"
// #include <xmlrpc-c/base.hpp>
// #include <xmlrpc-c/client_simple.hpp>

class XmlrpcController : XmlRpc::XmlRpcClient {
public:
  XmlrpcController();
  ~XmlrpcController();

  bool connectToServer(const std::string& serverUrl, const int port);
  void disconnectFromServer();
    XmlRpc::XmlRpcValue sinArgs, unArg, dosArgs, resultado;

  std::string sendRequest(const std::string& methodName, XmlRpc::XmlRpcValue& params);

    void activarBluetooth();
    void desactivarBluetooth();
    void activarMotores();
    void desactivarMotores();
    void moverAdelante();
    void moverAtras();
    void moverDerecha();
    void moverIzquierda();
    void detenerMovimiento();
    
private:
  XmlRpc::XmlRpcClient _client;
};

#endif
