#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/archivoController.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/archivoModel.hpp"
#include <iostream>

ArchivoController::ArchivoController(const char* archivo)
    : archivoModel(archivo)
{
}

ArchivoController::~ArchivoController()
{   
}

bool ArchivoController::guardarArchivoXml(const char* nombreArchivo, const std::string& contenido){
    // Guardar archivo recibido del servidor
    if (archivoModel.guardarArchivoXml(nombreArchivo, contenido)) {
        std::cout << "El archivo se guardó correctamente." << std::endl;
        return true;
    } else {
        std::cout << "Error al guardar el archivo." << std::endl;
        return false;
    }
}

void ArchivoController::solicitarArchivoXml(const char* nombreArchivo){
    // if
    try
    {
     if (archivoModel.leerArchivoXml(nombreArchivo))
        {
            std::cout << "\n * Se cargó el archivo satisfactoriamente" << std::endl;
        }
    }
    catch(const std::exception& e)
    {
        std::cout << "Hubo un problema al leer el archivo" << std::endl;
        std::cerr << e.what() << '\n';
    }
}
