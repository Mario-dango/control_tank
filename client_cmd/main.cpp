// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/archivoController.hpp"
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/archivoModel.hpp"
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/pugixml/pugiconfig.hpp"
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/pugixml/pugixml.hpp"
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/models_h/archivoModel.hpp"
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"
// #include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/views_h/cmdView.hpp"
#include "/home/bawy/Plantillas/git_poo/control_tank/client_cmd/resourse/lib/controllers_h/mainController.hpp"
#include <iostream>
#include <stdlib.h>

int main(int argc, char** argv) {
    MainController *mainController;
    // mainController = new MainController();
    mainController = new MainController("127.0.0.1", 8891);
    mainController->run();
    delete mainController;

    return 0;
}
