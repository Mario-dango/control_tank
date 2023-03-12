#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/archivoModel.hpp"
#include <iostream>

ArchivoModel::ArchivoModel(const char* nombreArchivo) {
    nombreArchivoXml = nombreArchivo;
}

ArchivoModel::~ArchivoModel() {
}

bool ArchivoModel::leerArchivoXml(const char* nombreArchivo){
    // Cargamos el archivo XML
    // doc.load_file("aa");
    if (!doc.load_file(nombreArchivo)) {
        std::cout << "Error al cargar el archivo XML." << std::endl;
        return false;
    }

    // Obtenemos el nodo raíz del documento
    pugi::xml_node logs = doc.child("logs");

    // Recorremos todos los elementos "log"
    for (pugi::xml_node log = logs.child("log"); log; log = log.next_sibling("log")) {
        // Obtenemos la fecha de la sesión
        std::string date = log.attribute("date").as_string();

        // Obtenemos el usuario
        std::string user = log.child_value("user");

        // Obtenemos la hora de conexión y desconexión
        std::string connect_time = log.child_value("connect");
        std::string disconnect_time = log.child_value("disconnect");

        // Imprimimos los detalles de la sesión
        std::cout << "Fecha: " << date << std::endl;
        std::cout << "Usuario: " << user << std::endl;
        std::cout << "Hora de conexión: " << connect_time << std::endl;

        // Recorremos todas las acciones registradas
        std::cout << "Acciones:" << std::endl;
        for (pugi::xml_node action = log.child("actions").child("move"); action; action = action.next_sibling()) {
            std::string name = action.child_value();
            std::string duration = action.attribute("duration").as_string();
            std::cout << "  " << name << " (duración: " << duration << " segundos)" << std::endl;
        }

        // Imprimimos la hora de desconexión
        std::cout << "Hora de desconexión: " << disconnect_time << std::endl;

        // Imprimimos una línea en blanco para separar las sesiones
        std::cout << std::endl;
    }

}

bool ArchivoModel::guardarArchivoXml(const char* nombreArchivo, const std::string& contenido) {
 pugi::xml_document doc;

// Verificar que el contenido XML recibido sea válido
pugi::xml_parse_result result = doc.load_string(contenido.c_str());
if (!result) {
    std::cerr << "Error al parsear el archivo XML: " << result.description() << std::endl;
    return false;
}

// Guardar el contenido en un archivo
try {
    if (!doc.save_file(nombreArchivo)) {
        throw std::runtime_error("Error al guardar el archivo XML.");
    }
} catch (const std::exception& e) {
    std::cerr << "Error al guardar el archivo XML: " << e.what() << std::endl;
    return false;
}

return true;
}
