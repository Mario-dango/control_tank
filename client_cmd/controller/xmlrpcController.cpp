
#include "../client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"

XmlrpcController::XmlrpcController() {
  // constructor
}

XmlrpcController::~XmlrpcController() {
  // destructor
}

bool XmlrpcController::connectToServer(const std::string& serverUrl) {
  _client.setServer(serverUrl);
  // realizar conexión con el servidor
}

void XmlrpcController::disconnectFromServer() {
  // cerrar conexión con el servidor
}

std::string XmlrpcController::sendRequest(const std::string& methodName, xmlrpc_c::paramList& params) {
  xmlrpc_c::value result;
  _client.call(methodName, params, &result);
  std::string response = xmlrpc_c::value_string(result);
  return response;
}

void XmlrpcController::activarBluetooth(){
    
}

catch(XmlRpc::XmlRpcException e){
