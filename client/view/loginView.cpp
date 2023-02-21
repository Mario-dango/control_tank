#include "../resourse/lib/views_h/inicioView.h"
#include "ui_inicio.h"

InicioView::InicioView(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::InicioView)
{
    ui->setupUi(this);
}
