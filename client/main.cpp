#include <QApplication>
#include "../client/resourse/lib/models_h/inicioModel.h"
#include "../client/resourse/lib/controllers_h/inicioController.h"
#include "../client/resourse/lib/views_h/inicioView.h"

#include "../client/resourse/lib/models_h/dashboardModel.h"
#include "../client/resourse/lib/controllers_h/dashboardController.h"
#include "../client/resourse/lib/views_h/dashboardView.h"

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
