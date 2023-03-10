
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/views_h/cmdView.hpp"
#include <ctype.h>

using namespace std;

CmdVista::CmdVista() {
    opciones = {
                "[1]. Activar Bluetooth",
                "[2]. Desactivar Bluetooth",
                "[3]. Activar Motores",
                "[4]. Desactivar Motores",
                "[5]. Mover adelante",
                "[6]. Mover atrás",
                "[7]. Mover derecha",
                "[8]. Mover izquierda",
                "[9]. Detener movimiento\n",
                "[10]. Mostrar menú nuevamente",
                "[11]. Solicitar registro archivo.xml",
                "[12]. Ayuda de comandos",
                "[13]. Limpiar la consola.",
                "[14]. Visualizar datos de conexión XML-RPC",
                "[15]. Cambiar datos de conexión XML-RPC",
                "[0]. Salir"
                };
/*
Para subrayar una palabra, se puede utilizar el carácter especial de control 
de formato ANSI "\033[4m" antes de la palabra, y el carácter especial de 
control de formato ANSI "\033[0m" después de la palabra para restaurar el 
formato normal de la consola.

  └───>
*/

    opcionesConAyuda = {
                "[1]. \033[4mActivar Bluetooth\033[0m \n └───> Se procede a activar la comunicación bluetooth al robot móvil del lado del servidor.",
                "[2]. \033[4mDesactivar Bluetooth\033[0m \n └───> Se procede a desactivar la comunicación bluetooth al robot móvil del lado del servidor.",
                "[3]. \033[4mActivar Motores\033[0m \n └───> Se procede a activar ambos motores del robot móvil del lado del servidor.",
                "[4]. \033[4mDesactivar Motores\033[0m \n └───> Se procede a desactivar ambos motores del robot móvil del lado del servidor.",
                "[5]. \033[4mMover adelante\033[0m \n └───> Se procede a enviar el comando para que el robot móvil del lado del servidor comience a AVANZAR hasta nuevo comando.",
                "[6]. \033[4mMover atrás\033[0m \n └───> Se procede a enviar el comando para que el robot móvil del lado del servidor comience a RETROCEDER hasta nuevo comando.",
                "[7]. \033[4mMover derecha\033[0m \n └───> Se procede a enviar el comando para que el robot móvil del lado del servidor comience a GIRAR A LA DERECHA hasta nuevo comando.",
                "[8]. \033[4mMover izquierda\033[0m \n └───> Se procede a enviar el comando para que el robot móvil del lado del servidor comience a GIRAR A LA IZQUIERDA hasta nuevo comando.",
                "[9]. \033[4mDetener movimiento\033[0m \n └───> Se procede a enviar el comando para que el robot móvil del lado del servidor DETENGA SU MOVIMIENTO hasta nuevo comando.\n",
                "[10]. \033[4mMostrar menú nuevamente\033[0m \n  └───> Se imprimirá nuevamente el menú de opciones del lado del cliente.",
                "[11]. \033[4mSolicitar registro archivo.xml\033[0m \n  └───> Se procede a pedir del lado del servidor un archivo de formato XML con todas las acciones realizadas por los diferentes usuarios que han usado al robot móvil.\n\tEl mismo será guardado en la carpeta \033[3marchivos/\033[0m con el nombre de \033[3mlog.xml\033[0m.",
                "[12]. \033[4mAyuda de comandos\033[0m \n  └───> VISTA ACTUAL",
                "[13]. \033[4mLimpiar la consola\033[0m \n  └───> Se procede a limpiar la pantalla para una mejor claridad en la visualización de los datos.",
                "[14]. \033[4mVisualizar datos de conexión XML-RPC\033[0m \n └───> Se procede a mostrar los datos actuales con los que se conecta el cliente XmlRpc (datos del servidor XmlRpc).",
                "[15]. \033[4mCambiar datos de conexión XML-RPC\033[0m \n └───> Se procede a cambiar los datos con los que se conecta el cliente XmlRpc al servidor XmlRpc.\n\tPara ello se requiere ingreso de la nueva dirección IP del host y del puerto de conexión referentes al servidor XmlRpc.",
                "[0]. \033[4mSalir\033[0m \n └───> Se procede a cerrar la aplicación del cliente."
                };
}

void CmdVista::mostrarMenu() {
    std::cout << "\n============= Menú de opciones =============" << std::endl;
    for (int j = 0; j < opciones.size(); j ++) {
        std::cout << opciones[j] << std::endl;
    }
    std::cout << "=============================================\n\n" << std::endl;
}

int CmdVista::leerOpcion() {
    std::string entrada;
    int opcion;
    std::cout << "Seleccione una opción: ";
    std::cin >> entrada;
    std::cin.ignore();   

    bool esNumero = true;
    // Verificar cada caracter de la cadena
    for (char c : entrada) {
        if (!isdigit(c)) {
            esNumero = false;
            cout << "Se ingresó: " << c << " y se reconoció como caracter." << endl;
            cout << "Favor de ingresar una opción valida, nada de caracteres." << endl;
            break;
        }
        else if (isdigit(c)){            
            try {
                opcion = std::stoi(entrada);
                // cout << "El numero ingresado es: " << opcion << endl;
            } catch (const std::exception& e) {
                cout << "La cadena ingresada no representa un numero entero valido." << endl;
            }
        }
    }
    return opcion;
}

void CmdVista::mostrarAyuda(){
    for (int i = 0; i < this->opcionesConAyuda.size(); i++) {
        std::cout << this->opcionesConAyuda[i] << std::endl;
    }  
    std::string help = "\n\033[4mRECUERDE QUE SOLO SE ADMITEN LOS NÚMEROS ENTRE CORCHETES.\033[0m\n";
    std::cout << help << std::endl;
    return;
}

std::string CmdVista::leerCadena() {
    std::string cadena;
    std::cout << "Ingrese una cadena: ";
    std::getline(std::cin, cadena);
    return cadena;
}

void CmdVista::limpiarConsola() {
    system("clear");
    std::cout << "Se ha limpiado la consola.\nRecuerde que ingresando el número 10 ve nuevamente el menú.\n" << std::endl;
}

std::string CmdVista::cambiarDatos(string atributo) {
    std::string cadena;
    std::cout << "Ingrese el valor del " + atributo + " que desea cambiar\n>";
    std::getline(std::cin, cadena);
    return cadena;
}

void CmdVista::imprimirEnConsola(std::string texto) {
    std::cout << texto << std::endl;
    return;
}

const char* CmdVista::pedirArchivo() {
    string archivo;
    std::cout << "Ingrese la ruta del archivo.xml incluyendo el mismo." << endl;
    std::cout << "Ruta desde donde está el programa: resourse/tarea1.xml" << endl;
    std::cout << ">";
    std::getline(std::cin, archivo);
    const char* puntero = archivo.c_str();
    return puntero;
}