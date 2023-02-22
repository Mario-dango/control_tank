#include "../resourse/lib/controllers_h/inicioController.h"
#include "../resourse/lib/models_h/inicioModel.h"
#include "../resourse/lib/views_h/inicioView.h"
#include "../resourse/lib/views_h/dashboardView.h"

InicioController::InicioController(InicioModel *modelo, InicioView *vista, QObject *parent)
    : QObject(parent), modelo(modelo), vista(vista)
{
    connect(vista, &InicioView::inicioSesionClicked, this, &InicioController::iniciarSesion);
}

void InicioController::iniciarSesion()
{
    modelo->setNombreUsuario(vista->nombreUsuario());
    modelo->setContrasena(vista->contrasena());

    if (modelo->credencialesValidas()) {
        DashboardView dashboardView;
        dashboardView.exec();
    } else {
        // Mostrar mensaje de error
    }
}


