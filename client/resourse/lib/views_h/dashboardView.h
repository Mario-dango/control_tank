#ifndef DASHBOARD_VIEW_H
#define DASHBOARD_VIEW_H

#include <QDialog>
#include <QMainWindow>
#include "../client/views/ui/control_bt_client_ui.h"

namespace Ui {
    class DashboardView;
}

class DashboardView : public QMainWindow
{
    Q_OBJECT

public:
    DashboardView(QWidget *parent = nullptr);
    ~DashboardView();


private:
    Ui::DashboardView *ui;
    QPushButton *loginButton;
};



#endif // CONTROL_BT_CLIENT_H
