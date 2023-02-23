#include "../resourse/lib/views_h/inicioView.h"
#include "../client/views/ui/ui_inicio.h"

// InicioView.cpp

InicioView::InicioView(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::InicioView)
{
    // Configuración de la vista de inicio de sesión
    ui->setupUi(this);
    // ...
}

InicioView::~InicioView()
{
    delete ui;
}

QString InicioView::nombreUsuario() const
{
    // Devuelve el texto del cuadro de texto del nombre de usuario
    return ui->usuarioLineEdit->text();
}

QString InicioView::contrasena() const
{
    // Devuelve el texto del cuadro de texto de la contraseña
    return ui->contrasenaLineEdit->text();
}
