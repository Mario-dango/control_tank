#ifndef CMDVISTA_HPP
#define CMDVISTA_HPP

#include <iostream>
#include <string>
#include <vector>
//  -lws2_32
// g++ -Wall -lws2_32 cliente_basico.cpp XmlRpcClient.cpp XmlRpcUtil.cpp XmlRpcValue.cpp XmlRpcSocket.cpp XmlRpcSource.cpp XmlRpcDispatch.cpp  -o cliente
// g++ -Wall cliente_basico.cpp XmlRpcClient.cpp XmlRpcUtil.cpp XmlRpcValue.cpp XmlRpcSocket.cpp XmlRpcSource.cpp XmlRpcDispatch.cpp -o cliente -l WS2_32
class CmdVista {
public:
    //  Se define el constructor de la clase CmdVista.
    CmdVista();
    //  Muestra las opciones del menú.
    void mostrarMenu();
    //  Toma lo ingresado por el usuario desde la consola.
    int leerOpcion();
    //  Muestra las opciones del menú con detalles.
    void mostrarAyuda();
    //  Imprimir un mensaje desde la consola.
    void imprimirEnConsola(std::string texto);
    //  Limpía la consola y deja un mensaje de que se ha limpiado.
    void limpiarConsola();
    //  Recibe la ruta y el nombre del archivo XML a enviar al servidor.
    const char* pedirArchivo();
    //  Lee una cadena de caracteres.
    std::string leerCadena();
    std::string cambiarDatos(std::string atributo);

private:
    //  Atributo vector con las opciones del cliente.
    std::vector<std::string> opciones;
    //  Atributo vector con las opciones y descripciones del cliente.
    std::vector<std::string> opcionesConAyuda;
};

#endif
