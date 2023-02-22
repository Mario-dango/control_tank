// #include "maincontroller.h"
// #include "iniciomodel.h"
#include "../client/resourse/lib/controllers_h/dashboardController.h"
#include "../client/resourse/lib/models_h/inicioModel.h"
#include "../client/resourse/lib/models_h/dashboardModel.h"
#include "../client/resourse/lib/views_h/dashboardView.h"
#include <QMessageBox>

DashboardController::DashboardController(InicioView *inicioView, DashboardModel *dashboardModel, QObject *parent)
    : QObject(parent)
    , m_inicioView(inicioView)
    // , m_dashboardModel(dashboardModel)
{
    // Conectamos la señal accepted() de la vista de inicio al slot onInicioAccepted()
    connect(m_inicioView, &InicioView::accepted, this, &DashboardController::onInicioAccepted);
}

DashboardController::~DashboardController()
{
}

void DashboardController::onInicioAccepted()
{
    // Creamos el modelo de inicio y validamos los datos
    InicioModel inicioModel;
    if (!inicioModel.validarUsuario(m_inicioView->usuario()) || !inicioModel.validarContrasena(m_inicioView->contrasena())) {
        QMessageBox::warning(m_inicioView, tr("Inicio de sesión"), tr("Usuario y/o contraseña incorrectos"));
        return;
    }
    
    // Cerramos la vista de inicio y abrimos la vista de panel principal
    m_inicioView->close();
    m_dashboardView->show();
}
