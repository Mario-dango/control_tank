#ifndef INICIOCONTROLLER_H
#define INICIOCONTROLLER_H

#include "../resourse/lib/models_h/inicioModel.h"
#include "../resourse/lib/views_h/inicioView.h"

class InicioController : public QObject
{
    Q_OBJECT

public:
    InicioController(InicioModel *modelo, InicioView *vista, QObject *parent = nullptr);

private slots:
    void iniciarSesion();

private:
    InicioModel *modelo;
    InicioView *vista;
};

#endif // INICIOCONTROLLER_H
