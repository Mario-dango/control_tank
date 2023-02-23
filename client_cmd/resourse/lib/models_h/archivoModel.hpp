#ifndef ARCHIVOMODEL_HPP
#define ARCHIVOMODEL_HPP

#include <string>
#include <vector>

#include "../client_cmd/resourse/lib/controllers_h/xmlrpc/xmlrpc.h"
namespace std{

class ArchivoModel {
public:
    ArchivoModel();
    ArchivoModel::~ArchivoModel();

    bool crearArchivoXml(string nombreArchivo, string usuario, string fecha, vector<string> acciones);
    bool leerArchivoXml(string nombreArchivo, vector<string>& registros);
    bool editarArchivoXml(string nombreArchivo, string usuario, string fecha, vector<string> acciones));
    bool eliminarArchivoXml(string nombreArchivo);

};
}
#endif // ARCHIVOMODEL_HPP
