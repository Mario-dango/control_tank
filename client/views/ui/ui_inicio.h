/********************************************************************************
** Form generated from reading UI file 'inicio.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef INICIO_UI_H
#define INICIO_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Inicio
{
public:
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_2;
    QLabel *titulo;
    QLabel *Imagen;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout_3;
    QLabel *lb_password;
    QLabel *lb_usuario;
    QPushButton *btn_registrar;
    QVBoxLayout *verticalLayout_5;
    QLineEdit *le_usuario;
    QLineEdit *lineEdit;
    QPushButton *btn_ingresar;

    void setupUi(QWidget *Inicio)
    {
        if (Inicio->objectName().isEmpty())
            Inicio->setObjectName("Inicio");
        Inicio->resize(500, 450);
        Inicio->setMinimumSize(QSize(500, 300));
        Inicio->setMaximumSize(QSize(1024, 786));
        Inicio->setStyleSheet(QString::fromUtf8("background-color: rgb(7, 52, 255);\n"
"\n"
""));
        verticalLayoutWidget = new QWidget(Inicio);
        verticalLayoutWidget->setObjectName("verticalLayoutWidget");
        verticalLayoutWidget->setGeometry(QRect(40, 10, 415, 426));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_2->setSpacing(4);
        verticalLayout_2->setObjectName("verticalLayout_2");
        verticalLayout_2->setSizeConstraint(QLayout::SetFixedSize);
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        titulo = new QLabel(verticalLayoutWidget);
        titulo->setObjectName("titulo");
        titulo->setMinimumSize(QSize(400, 100));
        titulo->setMaximumSize(QSize(400, 200));
        QFont font;
        font.setFamilies({QString::fromUtf8("Kristen ITC")});
        font.setPointSize(24);
        titulo->setFont(font);

        verticalLayout_2->addWidget(titulo);

        Imagen = new QLabel(verticalLayoutWidget);
        Imagen->setObjectName("Imagen");
        Imagen->setMinimumSize(QSize(350, 200));
        Imagen->setMaximumSize(QSize(350, 200));
        Imagen->setStyleSheet(QString::fromUtf8("border: 5px solid black;"));
        Imagen->setPixmap(QPixmap(QString::fromUtf8("../../../../on_linux/poo_libre/imagenes/tank000.png")));
        Imagen->setScaledContents(true);
        Imagen->setAlignment(Qt::AlignCenter);
        Imagen->setMargin(0);

        verticalLayout_2->addWidget(Imagen, 0, Qt::AlignHCenter|Qt::AlignVCenter);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName("verticalLayout_3");
        lb_password = new QLabel(verticalLayoutWidget);
        lb_password->setObjectName("lb_password");
        lb_password->setMinimumSize(QSize(100, 20));
        lb_password->setMaximumSize(QSize(100, 80));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Noto Sans")});
        font1.setPointSize(10);
        font1.setBold(true);
        lb_password->setFont(font1);

        verticalLayout_3->addWidget(lb_password);

        lb_usuario = new QLabel(verticalLayoutWidget);
        lb_usuario->setObjectName("lb_usuario");
        lb_usuario->setMinimumSize(QSize(100, 20));
        lb_usuario->setMaximumSize(QSize(100, 80));
        lb_usuario->setFont(font1);

        verticalLayout_3->addWidget(lb_usuario);

        btn_registrar = new QPushButton(verticalLayoutWidget);
        btn_registrar->setObjectName("btn_registrar");
        btn_registrar->setStyleSheet(QString::fromUtf8("background-color: rgb(178, 55, 255);"));

        verticalLayout_3->addWidget(btn_registrar);


        horizontalLayout->addLayout(verticalLayout_3);

        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setObjectName("verticalLayout_5");
        verticalLayout_5->setSizeConstraint(QLayout::SetFixedSize);
        le_usuario = new QLineEdit(verticalLayoutWidget);
        le_usuario->setObjectName("le_usuario");
        le_usuario->setMinimumSize(QSize(300, 20));
        le_usuario->setMaximumSize(QSize(350, 20));

        verticalLayout_5->addWidget(le_usuario);

        lineEdit = new QLineEdit(verticalLayoutWidget);
        lineEdit->setObjectName("lineEdit");

        verticalLayout_5->addWidget(lineEdit);

        btn_ingresar = new QPushButton(verticalLayoutWidget);
        btn_ingresar->setObjectName("btn_ingresar");
        btn_ingresar->setStyleSheet(QString::fromUtf8("background-color: rgb(178, 55, 255);"));

        verticalLayout_5->addWidget(btn_ingresar);


        horizontalLayout->addLayout(verticalLayout_5);


        verticalLayout_2->addLayout(horizontalLayout);


        retranslateUi(Inicio);

        QMetaObject::connectSlotsByName(Inicio);
    } // setupUi

    void retranslateUi(QWidget *Inicio)
    {
        Inicio->setWindowTitle(QCoreApplication::translate("Inicio", "Form", nullptr));
        titulo->setText(QCoreApplication::translate("Inicio", "    Inicio de sesi\303\263n", nullptr));
        Imagen->setText(QString());
        lb_password->setText(QCoreApplication::translate("Inicio", "Contrase\303\261a:", nullptr));
        lb_usuario->setText(QCoreApplication::translate("Inicio", "Usuario:", nullptr));
        btn_registrar->setText(QCoreApplication::translate("Inicio", "registrar", nullptr));
        btn_ingresar->setText(QCoreApplication::translate("Inicio", "Ingresar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Inicio: public Ui_Inicio {};
} // namespace Ui

QT_END_NAMESPACE

#endif // INICIO_UI_H
