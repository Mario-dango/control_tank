/********************************************************************************
** Form generated from reading UI file 'control_bt_client.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef CONTROL_BT_CLIENT_UI_H
#define CONTROL_BT_CLIENT_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QFrame *frame_arriba;
    QLabel *autor;
    QWidget *layoutWidget;
    QGridLayout *gridLayout;
    QPushButton *btn_retroceder;
    QPushButton *btn_detener;
    QPushButton *on_off_bt;
    QPushButton *btn_avanzar;
    QPushButton *btn_izquierda;
    QLabel *t_botones;
    QComboBox *bt_list;
    QRadioButton *on_off_motor;
    QPushButton *btn_derecha;
    QPushButton *on_off_server;
    QPushButton *pushButton;
    QLabel *label;
    QLabel *Imagen_2;
    QFrame *frame_abajo;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout_2;
    QLabel *label_2;
    QListWidget *r_log;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1035, 617);
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: rgb(97, 53, 131);"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setObjectName("horizontalLayout");
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(0);
        verticalLayout->setObjectName("verticalLayout");
        frame_arriba = new QFrame(centralwidget);
        frame_arriba->setObjectName("frame_arriba");
        frame_arriba->setFrameShape(QFrame::StyledPanel);
        frame_arriba->setFrameShadow(QFrame::Raised);
        autor = new QLabel(frame_arriba);
        autor->setObjectName("autor");
        autor->setGeometry(QRect(20, 210, 691, 51));
        layoutWidget = new QWidget(frame_arriba);
        layoutWidget->setObjectName("layoutWidget");
        layoutWidget->setGeometry(QRect(370, 20, 601, 231));
        gridLayout = new QGridLayout(layoutWidget);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(0, 0, 0, 0);
        btn_retroceder = new QPushButton(layoutWidget);
        btn_retroceder->setObjectName("btn_retroceder");

        gridLayout->addWidget(btn_retroceder, 4, 1, 1, 1);

        btn_detener = new QPushButton(layoutWidget);
        btn_detener->setObjectName("btn_detener");

        gridLayout->addWidget(btn_detener, 3, 1, 1, 1);

        on_off_bt = new QPushButton(layoutWidget);
        on_off_bt->setObjectName("on_off_bt");

        gridLayout->addWidget(on_off_bt, 1, 3, 1, 1);

        btn_avanzar = new QPushButton(layoutWidget);
        btn_avanzar->setObjectName("btn_avanzar");
        btn_avanzar->setAutoDefault(true);

        gridLayout->addWidget(btn_avanzar, 2, 1, 1, 1);

        btn_izquierda = new QPushButton(layoutWidget);
        btn_izquierda->setObjectName("btn_izquierda");

        gridLayout->addWidget(btn_izquierda, 3, 0, 1, 1);

        t_botones = new QLabel(layoutWidget);
        t_botones->setObjectName("t_botones");

        gridLayout->addWidget(t_botones, 1, 0, 1, 1);

        bt_list = new QComboBox(layoutWidget);
        bt_list->addItem(QString());
        bt_list->addItem(QString());
        bt_list->setObjectName("bt_list");

        gridLayout->addWidget(bt_list, 0, 3, 1, 1);

        on_off_motor = new QRadioButton(layoutWidget);
        on_off_motor->setObjectName("on_off_motor");

        gridLayout->addWidget(on_off_motor, 0, 0, 1, 3);

        btn_derecha = new QPushButton(layoutWidget);
        btn_derecha->setObjectName("btn_derecha");

        gridLayout->addWidget(btn_derecha, 3, 2, 1, 1);

        on_off_server = new QPushButton(layoutWidget);
        on_off_server->setObjectName("on_off_server");

        gridLayout->addWidget(on_off_server, 2, 3, 1, 1);

        pushButton = new QPushButton(layoutWidget);
        pushButton->setObjectName("pushButton");

        gridLayout->addWidget(pushButton, 5, 3, 1, 1);

        label = new QLabel(layoutWidget);
        label->setObjectName("label");

        gridLayout->addWidget(label, 4, 3, 1, 1);

        Imagen_2 = new QLabel(frame_arriba);
        Imagen_2->setObjectName("Imagen_2");
        Imagen_2->setGeometry(QRect(10, 10, 350, 200));
        Imagen_2->setMinimumSize(QSize(350, 200));
        Imagen_2->setMaximumSize(QSize(350, 200));
        Imagen_2->setStyleSheet(QString::fromUtf8("border: 5px solid black;"));
        Imagen_2->setPixmap(QPixmap(QString::fromUtf8("../../../../on_linux/poo_libre/imagenes/tank000.png")));
        Imagen_2->setScaledContents(true);
        Imagen_2->setAlignment(Qt::AlignCenter);
        Imagen_2->setMargin(0);

        verticalLayout->addWidget(frame_arriba);

        frame_abajo = new QFrame(centralwidget);
        frame_abajo->setObjectName("frame_abajo");
        frame_abajo->setAutoFillBackground(false);
        frame_abajo->setStyleSheet(QString::fromUtf8("background-color: rgb(28, 113, 216);"));
        frame_abajo->setFrameShape(QFrame::StyledPanel);
        frame_abajo->setFrameShadow(QFrame::Raised);
        verticalLayoutWidget = new QWidget(frame_abajo);
        verticalLayoutWidget->setObjectName("verticalLayoutWidget");
        verticalLayoutWidget->setGeometry(QRect(10, 14, 971, 251));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout_2->setSpacing(12);
        verticalLayout_2->setObjectName("verticalLayout_2");
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        label_2 = new QLabel(verticalLayoutWidget);
        label_2->setObjectName("label_2");

        verticalLayout_2->addWidget(label_2);

        r_log = new QListWidget(verticalLayoutWidget);
        r_log->setObjectName("r_log");

        verticalLayout_2->addWidget(r_log);


        verticalLayout->addWidget(frame_abajo);


        horizontalLayout->addLayout(verticalLayout);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 1035, 22));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        autor->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        btn_retroceder->setText(QCoreApplication::translate("MainWindow", "Retroceder", nullptr));
        btn_detener->setText(QCoreApplication::translate("MainWindow", "Detener", nullptr));
        on_off_bt->setText(QCoreApplication::translate("MainWindow", "Conectar dispositivo Bluetooth", nullptr));
        btn_avanzar->setText(QCoreApplication::translate("MainWindow", "Avanzar", nullptr));
        btn_izquierda->setText(QCoreApplication::translate("MainWindow", "Izquierda", nullptr));
        t_botones->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
        bt_list->setItemText(0, QCoreApplication::translate("MainWindow", "98:D3:31:FC:96:5F - HC-06", nullptr));
        bt_list->setItemText(1, QCoreApplication::translate("MainWindow", "94:17:00:DD:74:5F - Bawy~", nullptr));

        on_off_motor->setText(QCoreApplication::translate("MainWindow", "Activar / Desactivar Motores", nullptr));
        btn_derecha->setText(QCoreApplication::translate("MainWindow", "Derecha", nullptr));
        on_off_server->setText(QCoreApplication::translate("MainWindow", "Bot\303\263n Servidor", nullptr));
        pushButton->setText(QCoreApplication::translate("MainWindow", "Cerrar sesi\303\263n", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Logueado c\303\263mo: ", nullptr));
        Imagen_2->setText(QString());
        label_2->setText(QCoreApplication::translate("MainWindow", "TextLabel", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // CONTROL_BT_CLIENT_UI_H
