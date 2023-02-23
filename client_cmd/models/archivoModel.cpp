#include "../client_cmd/resourse/lib/models_h/archivoModel.hpp"


ArchivoModel::ArchivoModel() {
}


ArchivoModel::~ArchivoModel() {
}

bool ArchivoModel::crearArchivoXml() {
    xmlrpc_c::paramList parametros;
    parametros.add(xmlrpc_c::value_string(nombreArchivo));
    std::string resultado = cliente.call(urlServidor, "crear_archivo_xml", parametros);
    return (resultado == "OK");
}

bool ArchivoModel::leerArchivoXml() {
    xmlrpc_c::paramList parametros;
    parametros.add(xmlrpc_c::value_string(nombreArchivo));
    std::string resultado = cliente.call(urlServidor, "leer_archivo_xml", parametros);
    if (resultado != "ERROR") {
        // Analizar el resultado y llenar los vectores de datos
        // ...
        return true;
    } else {
        return false;
    }
}

bool ArchivoModel::eliminarArchivoXml() {
    xmlrpc_c::paramList parametros;
    parametros.add(xmlrpc_c::value_string(nombreArchivo));
    std::string resultado = cliente.call(urlServidor, "eliminar_archivo_xml", parametros);
    return (resultado == "OK");
}

bool ArchivoModel::agregarRegistro(const std::string& fecha, const std::string& usuario, const std::string& accion, const std::string& duracion) {
    xmlrpc_c::paramList parametros;
    parametros.add(xmlrpc_c::value_string(nombreArchivo));
    parametros.add(xmlrpc_c::value_string(fecha));
    parametros.add(xmlrpc_c::value_string(usuario));
    parametros.add(xmlrpc_c::value_string(accion));
    parametros.add(xmlrpc_c::value_string(duracion));
    std::string resultado = cliente.call(urlServidor, "agregar_registro", parametros);
    return (resultado == "OK");
}
