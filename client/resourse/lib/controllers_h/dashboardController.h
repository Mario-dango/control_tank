#ifndef DASHBOARD_CONTROLLER_H
#define DASHBOARD_CONTROLLER_H

// #include "inicioview.h"
// #include "dashboardview.h"
#include "../client/resourse/lib/views_h/dashboardView.h"
#include "../client/resourse/lib/views_h/inicioView.h"


class DashboardController : public QObject
{
    Q_OBJECT
    
public:
    explicit DashboardController(InicioView *inicioView, DashboardModel *dashboardModel, QObject *parent = nullptr);
    virtual ~DashboardController();
    
private slots:
    void onInicioAccepted();
    
private:
    InicioView *m_inicioView;
    DashboardController *m_dashboardModel;
};

#endif // MAINCONTROLLER_H
