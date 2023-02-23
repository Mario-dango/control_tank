#include <iostream>
#include <conio.h>

int main() {
    char input;

    while (true) {
        // Imprimir un prompt para el usuario
        std::cout << "> ";

        // Leer la tecla presionada por el usuario
        input = _getch();

        // Realizar alguna acción basada en la tecla presionada
        if (input == 'q') {
            break;
        } else if (input == 'h') {
            // Limpiar la pantalla
            system("cls");
            std::cout << "Este es un ejemplo de una interfaz estilo cmd en C++.\n"
                      << "Los siguientes comandos están disponibles:\n"
                      << "  q - Salir del programa\n"
                      << "  h - Limpiar la pantalla y mostrar este mensaje de ayuda\n";
        } else {
            std::cout << "Tecla no reconocida. Presione 'h' para ver la ayuda.\n";
        }
    }

    return 0;
}