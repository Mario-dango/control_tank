#pragma once
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"
using namespace std;

// constructor
XmlrpcController::XmlrpcController(const char* host, int port)
 : XmlRpc::XmlRpcClient(host, port)
{
    // XmlRpc::XmlRpcClient _client();
    CmdVista consola;
    this->host = host;
    this->port = port;
}

XmlrpcController::~XmlrpcController() {
  // destructor
}

// para habilitar una conexión a la espera de terminar se unsa de XmlRpcClient el siguiente método
// executeNonBlock
// void XmlrpcController::disconnectFromServer() {
//   // cerrar conexión con el servidor
//   this->close();
// }


int XmlrpcController::get_puerto(){
  return this->port;
}

const char* XmlrpcController::get_host(){
  return this->host;
}

const char* XmlrpcController::set_host(const char* servidorHost){
  this->host = servidorHost;
  return this->host;
}

int XmlrpcController::set_puerto(int puerto){
  this->port = puerto;
  return this->port;
}

bool XmlrpcController::enviar(const int caso){
  const char* metodo;
  // cout << "Puerto: " << this->port << "\nDirección: " << this->host << endl;
  switch (caso)
  {
    // consola.imprimirEnConsola("antes de los casos");
  case 1:
    // metodo = "activar_bluetooth";
    metodo = "bluetooth";
    break;
  case 2:
    // metodo = "desactivar_bluetooth";
    metodo = "bluetooth";
    break;
  case 3:
    // metodo = "activar_motor";
    metodo = "motores";
    break;
  case 4:
    // metodo = "desactivar_motor";
    metodo = "motores";
    break;
  case 5:
    metodo = "avanzar";
    break;
  case 6:
    metodo = "retroceder";
    break;
  case 7:
    metodo = "derecha";
    break;
  case 8:
    metodo = "izquierda";
    break;
  case 9:
    metodo = "detenerse";
    break;
  default:
    return false;
  }

    // consola.imprimirEnConsola("fuera del switch");
  try{
    //
    // consola.imprimirEnConsola("dentro del try");
    bool exito = this->execute(metodo, parametro, resultado);
    if (exito){
      //  La llamada al método fue exitosa.
      consola.imprimirEnConsola("exito en la llamda");
      return resultado;
    } else {
      //  La llamada al método ha fallado
      return false;
    }
  }
  catch(XmlRpc::XmlRpcException e){
    cout << "Error numero " << e.getCode() << ", " << e.getMessage() << "\r\n";
    consola.imprimirEnConsola("Re loco no funca");
    return false;
    // std::cerr << e.what() << '\n';
  }
}

bool XmlrpcController::activarBluetooth(){
    // consola.imprimirEnConsola("Intento de activar BT");
  return this->enviar(1);
}

bool XmlrpcController::desactivarBluetooth(){
  return this->enviar(2);
}

bool XmlrpcController::activarMotores(){
  return this->enviar(3);
}

bool XmlrpcController::desactivarMotores(){
  return this->enviar(4);
}

bool XmlrpcController::moverAdelante(){
  return this->enviar(5);
}

bool XmlrpcController::moverAtras(){
  return this->enviar(6);
}

bool XmlrpcController::moverDerecha(){
  return this->enviar(7);
}

bool XmlrpcController::moverIzquierda(){
  return this->enviar(8);
}

bool XmlrpcController::detenerMovimiento(){
  return this->enviar(9);
}
///////////////////// Definir cómo pasar la ruta del archivo.xml
bool XmlrpcController::solicitarArchivoRegistro(){
  try{
    const char* metodo;
    metodo = "solicitarXml";
    bool exito = this->execute(metodo, this->data, this->resultado);  
    if (exito){
      consola.imprimirEnConsola("exito en la llamda XML");
      return true;
    }
    else{
      return false;
    }
  }catch(XmlRpc::XmlRpcException& e) {
    std::cerr << "Error en la llamada a XML-RPC: " <<  std::endl;
    std::cerr << "Código de error: " << e.getCode() << std::endl;
    return false;
}
}
