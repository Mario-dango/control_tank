/********************************************************************************
** Form generated from reading UI file 'registro.ui'
**
** Created by: Qt User Interface Compiler version 6.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef REGISTRO_UI_H
#define REGISTRO_UI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Form
{
public:
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout_3;
    QLabel *label_4;
    QLineEdit *lineEdit_3;
    QLabel *label_3;
    QLabel *label_5;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_3;
    QLineEdit *lineEdit_4;
    QLineEdit *lineEdit;
    QLabel *label_6;
    QLabel *label_2;
    QPushButton *pushButton_2;

    void setupUi(QWidget *Form)
    {
        if (Form->objectName().isEmpty())
            Form->setObjectName("Form");
        Form->resize(428, 380);
        Form->setMinimumSize(QSize(400, 380));
        Form->setMaximumSize(QSize(1024, 786));
        Form->setStyleSheet(QString::fromUtf8("background-color: rgb(152, 51, 202);"));
        gridLayoutWidget = new QWidget(Form);
        gridLayoutWidget->setObjectName("gridLayoutWidget");
        gridLayoutWidget->setGeometry(QRect(20, 20, 382, 311));
        gridLayout_3 = new QGridLayout(gridLayoutWidget);
        gridLayout_3->setObjectName("gridLayout_3");
        gridLayout_3->setContentsMargins(0, 0, 0, 0);
        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName("label_4");

        gridLayout_3->addWidget(label_4, 3, 0, 1, 1);

        lineEdit_3 = new QLineEdit(gridLayoutWidget);
        lineEdit_3->setObjectName("lineEdit_3");

        gridLayout_3->addWidget(lineEdit_3, 3, 1, 1, 1);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName("label_3");

        gridLayout_3->addWidget(label_3, 4, 0, 1, 1);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName("label_5");

        gridLayout_3->addWidget(label_5, 1, 0, 1, 1);

        lineEdit_2 = new QLineEdit(gridLayoutWidget);
        lineEdit_2->setObjectName("lineEdit_2");

        gridLayout_3->addWidget(lineEdit_2, 4, 1, 1, 1);

        pushButton_3 = new QPushButton(gridLayoutWidget);
        pushButton_3->setObjectName("pushButton_3");
        pushButton_3->setStyleSheet(QString::fromUtf8("background-color: rgb(79, 79, 255);"));

        gridLayout_3->addWidget(pushButton_3, 6, 0, 1, 1);

        lineEdit_4 = new QLineEdit(gridLayoutWidget);
        lineEdit_4->setObjectName("lineEdit_4");

        gridLayout_3->addWidget(lineEdit_4, 1, 1, 1, 1);

        lineEdit = new QLineEdit(gridLayoutWidget);
        lineEdit->setObjectName("lineEdit");

        gridLayout_3->addWidget(lineEdit, 5, 1, 1, 1);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName("label_6");
        QFont font;
        font.setFamilies({QString::fromUtf8("Miriam Libre")});
        font.setPointSize(18);
        label_6->setFont(font);
        label_6->setStyleSheet(QString::fromUtf8("background-color: rgb(79, 79, 255);\n"
"\n"
""));

        gridLayout_3->addWidget(label_6, 0, 0, 1, 2);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName("label_2");

        gridLayout_3->addWidget(label_2, 5, 0, 1, 1);

        pushButton_2 = new QPushButton(gridLayoutWidget);
        pushButton_2->setObjectName("pushButton_2");
        pushButton_2->setStyleSheet(QString::fromUtf8("background-color: rgb(79, 79, 255);"));

        gridLayout_3->addWidget(pushButton_2, 6, 1, 1, 1);


        retranslateUi(Form);

        QMetaObject::connectSlotsByName(Form);
    } // setupUi

    void retranslateUi(QWidget *Form)
    {
        Form->setWindowTitle(QCoreApplication::translate("Form", "Form", nullptr));
        label_4->setText(QCoreApplication::translate("Form", "Apellido:", nullptr));
        label_3->setText(QCoreApplication::translate("Form", "Correo:", nullptr));
        label_5->setText(QCoreApplication::translate("Form", "Nombre:", nullptr));
        pushButton_3->setText(QCoreApplication::translate("Form", "Vovler", nullptr));
        label_6->setText(QCoreApplication::translate("Form", "Registraci\303\263n de Usuario", nullptr));
        label_2->setText(QCoreApplication::translate("Form", "Usuario habilitado:", nullptr));
        pushButton_2->setText(QCoreApplication::translate("Form", "Registrar", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Form: public Ui_Form {};
} // namespace Ui

QT_END_NAMESPACE

#endif // REGISTRO_UI_H
