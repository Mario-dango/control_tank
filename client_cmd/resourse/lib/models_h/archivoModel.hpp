#ifndef ARCHIVOMODEL_HPP
#define ARCHIVOMODEL_HPP

#include <string>
#include <vector>
#include <string>
#include <ctime>

// #include "xmlrpc/xmlrpc.h"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/pugixml/pugiconfig.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/pugixml/pugixml.hpp"

class ArchivoModel : public pugi::xml_document
// , public pugi::xml_node
{

    private:
        // Creamos un objeto XML vacío
        xml_document doc;
        // Añadimos el elemento raíz del documento
        xml_node logs;
        xml_node log;
        xml_node usuarios;
        xml_node conectado;
        xml_node acciones;
        xml_node accion;
        xml_node desconectado;

        const char* nombreArchivoXml;
    public:
        ArchivoModel(const char* nombreArchivo);
        ~ArchivoModel();
        // // char* nombre;
        // bool crearArchivoXml();
        // bool crearArchivoXml(const char* nombreArchivo);
        bool guardarArchivoXml(const char* nombreArchivo, const std::string& contenido);
        bool leerArchivoXml(const char* nombreArchivo);
        // bool editarArchivoXml(std::string nombreArchivo, std::string usuario, std::string fecha, std::vector<std::string> acciones);
        // bool eliminarArchivoXml(std::string nombreArchivo);

};

#endif // ARCHIVOMODEL_HPP
