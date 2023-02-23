#ifndef ARCHIVOCONTROLLER_H
#define ARCHIVOCONTROLLER_H

#include "../client_cmd/resourse/lib/models_h/archivoModel.hpp"

class ArchivoController {
private:
    ArchivoModel archivoModel;
public:
    ArchivoController();
    void crearArchivo();
    void leerArchivo();
    void eliminarArchivo();
};

#endif //ARCHIVOCONTROLLER_H
