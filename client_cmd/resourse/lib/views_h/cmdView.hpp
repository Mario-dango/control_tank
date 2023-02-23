#ifndef CMDVISTA_HPP
#define CMDVISTA_HPP

#include <iostream>
#include <string>
#include <vector>

class CmdVista {
public:
    CmdVista();

    void mostrarMenu();
    int leerOpcion();
    void mostrarAyuda();
    std::string leerCadena();
    void mostrarMensaje(std::string mensaje);

private:
    std::vector<std::string> opciones;
};

#endif
