#ifndef MAINCONTROLLER_HPP
#define MAINCONTROLLER_HPP

#include "../client_cmd/resourse/lib/views_h/cmdView.hpp"
#include "../client_cmd/resourse/lib/controllers_h/archivoController.hpp"
#include "../client_cmd/resourse/lib/controllers_h/xmlrpcController.hpp"

class MainController {
public:
    MainController();
    void run();

private:
    CmdVista cmdVista;
    ArchivoController archivoController;
    XmlrpcController xmlrpcController;
};

#endif // MAINCONTROLLER_HPP
