#ifndef INICIO_VIEW_H
#define INICIO_VIEW_H

#include <QMainWindow>
// #include "../client/views/ui/ui_inicio.h"


QT_BEGIN_NAMESPACE
namespace Ui { class InicioView; }
QT_END_NAMESPACE
class InicioView : public QMainWindow
{
    Q_OBJECT

public:
    explicit InicioView(QWidget *parent = nullptr);
    ~InicioView();

    QString nombreUsuario() const;
    QString contrasena() const;

signals:
    void inicioSesionClicked();

private:
    Ui::InicioView *ui;
};

#endif // INICIOVIEW_H
