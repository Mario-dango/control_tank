#include "../client_cmd/resourse/lib/controllers_h/archivoController.hpp"
#include "../client_cmd/resourse/lib/models_h/archivoModel.hpp"
#include <iostream>
#include <fstream>


void ArchivoController::crearArchivo(std::string nombre, std::string contenido){
    // Abrir el archivo en modo escritura
    std::ofstream archivo(nombre + ".txt", std::ios::out);
    
    // Verificar si se pudo abrir el archivo
    if(!archivo.is_open()){
        std::cout << "No se pudo abrir el archivo" << std::endl;
        return;
    }
    
    // Escribir el contenido en el archivo
    archivo << contenido;
    
    // Cerrar el archivo
    archivo.close();
}

void ArchivoController::editarArchivo(const std::string& nombreArchivo) {
    // Abrir el archivo
    std::ifstream archivo(nombreArchivo);
    if (!archivo) {
        std::cout << "No se pudo abrir el archivo " << nombreArchivo << std::endl;
        return;
    }
    
    // Leer el contenido del archivo en una cadena
    std::stringstream buffer;
    buffer << archivo.rdbuf();
    std::string contenido = buffer.str();
    archivo.close();
    
    // Modificar el contenido
    // (aquí puedes agregar tu lógica para modificar el contenido del archivo)
    
    // Guardar el contenido modificado en el archivo
    std::ofstream archivoSalida(nombreArchivo);
    if (!archivoSalida) {
        std::cout << "No se pudo guardar el archivo " << nombreArchivo << std::endl;
        return;
    }
    archivoSalida << contenido;
    archivoSalida.close();
}


std::string ArchivoController::leerArchivo(std::string nombre){
    // Abrir el archivo en modo lectura
    std::ifstream archivo(nombre + ".txt", std::ios::in);
    std::string contenido;
    std::string linea;
    
    // Verificar si se pudo abrir el archivo
    if(!archivo.is_open()){
        std::cout << "No se pudo abrir el archivo" << std::endl;
        return "";
    }
    
    // Leer el contenido del archivo
    while(getline(archivo, linea)){
        contenido += linea + "\n";
    }
    
    // Cerrar el archivo
    archivo.close();
    
    return contenido;
}

bool ArchivoController::borrarArchivo(std::string nombre){
    // Eliminar el archivo
    if(remove((nombre + ".txt").c_str()) != 0){
        std::cout << "No se pudo eliminar el archivo" << std::endl;
        return false;
    }
    
    return true;
}
