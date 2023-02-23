#include "../client_cmd/resourse/lib/controllers_h/mainController.hpp"

MainController::MainController() {}

void MainController::run() {
    // Inicializar las clases que necesitan ser iniciadas
    // archivoController.init();
    xmlrpcController.init();

    // Ejecutar la aplicación
    while (true) {
        int opcion = cmdVista mostrarMenu();
        switch (opcion) {
            case 1:
                xmlrpcController.activarBluetooth();
                break;
            case 2:
                xmlrpcController.desactivarBluetooth();
                break;
            case 3:
                xmlrpcController.activarMotores();
                break;
            case 4:
                xmlrpcController.desactivarMotores();
                break;
            case 5:
                xmlrpcController.moverAdelante();
                break;
            case 6:
                xmlrpcController.moverAtras();
                break;
            case 7:
                xmlrpcController.moverDerecha();
                break;
            case 8:
                xmlrpcController.moverIzquierda();
                break;
            case 9:
                xmlrpcController.detenerMovimiento();
                break;
            case 10:
                cmdVista.mostrarAyuda();
                break;
            case 11:
                archivoController.solicitarArchivoXml();
                break;
            case 12:
                archivoController.enviarArchivoXml();
                break;
            case 13:
                return;
        }
    }
}

int main() {
    MainController mainController;
    mainController.run();
    return 0;
}