#ifndef INICIO_VIEW_H
#define INICIO_VIEW_H

#include <QDialog>

namespace Ui {
class InicioView;
}

class InicioView : public QDialog
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
