#ifndef ARCHIVOCONTROLLER_H
#define ARCHIVOCONTROLLER_H
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/archivoModel.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/archivoController.hpp"

class ArchivoController {
private:
    ArchivoModel archivoModel;
public:
    ArchivoController(const char* nombre);
    ~ArchivoController();
    // void crearArchivo();
    void solicitarArchivoXml(const char* nombreArchivo);
    bool guardarArchivoXml(const char* nombreArchivo, const std::string& contenido);
    // void eliminarArchivo();

};

#endif //ARCHIVOCONTROLLER_H
