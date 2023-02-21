#include <QApplication>
#include "resourse/lib/models_h/inicioModel.h"
#include "resourse/lib/controllers_h/inicioController.h"
#include "resourse/lib/views_h/inicioView.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    InicioModel inicioModel;
    InicioView inicioView;
    InicioController inicioController(&inicioModel, &inicioView);

    DashboardModel dashboardModel;
    DashboardView dashboardView;
    DashboardController dashboardController(&dashboardModel, &dashboardView);

    inicioView.show();

    return app.exec();
}
