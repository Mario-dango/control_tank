#include "../client_cmd/resourse/lib/views_h/cmdView.hpp"

CmdVista::CmdVista() {
    opciones = {"1. Activar/Desactivar Bluetooth",
                "2. Activar/Desactivar motores",
                "3. Mover adelante",
                "4. Mover atrás",
                "5. Mover derecha",
                "6. Mover izquierda",
                "7. Detener movimiento",
                "8. Ayuda de comandos",
                "9. Solicitar archivo XML",
                "10. Enviar archivo XML",
                "11. Salir"};
}

void CmdVista::mostrarMenu() {
    std::cout << "---- Menú de opciones ----" << std::endl;
    for (auto opcion : opciones) {
        std::cout << opcion << std::endl;
    }
}

int CmdVista::leerOpcion() {
    int opcion;
    std::cout << "Seleccione una opción: ";
    std::cin >> opcion;
    std::cin.ignore();
    return opcion;
}

void mostrarAyuda(){
    CmdVista mostrarMenu();
}

std::string CmdVista::leerCadena() {
    std::string cadena;
    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, cadena);
    return cadena;
}

void CmdVista::mostrarMensaje(std::string mensaje) {
    std::cout << mensaje << std::endl;
}
