QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    main.cpp \
    models/inicioModel.cpp \
    models/robotModel.cpp \

    controllers/inicioController.cpp \
    controllers/dashboardController.cpp \
    controllers/registrarController.cpp \

    models/inicioModel.cpp \
    models/dashboardModel.cpp \
    models/registrarModel.cpp \
    
    views/inicioView.cpp \
    views/dashboardView.cpp \
    views/registrarView.cpp \

HEADERS += \
    models/inicioModel.h \
    models/robotModel.h 

    controllers/inicioController.h \
    controllers/dashboardController.h \
    controllers/registrarController.h \

    models/inicioModel.h \
    models/dashboardModel.h \
    models/registrarModel.h \
    
    views/inicioView.h \
    views/dashboardView.h \
    views/registrarView.h

FORMS += \
    views/ui/control_bt_client.ui \
    views/ui/inicio.ui \
    views/ui/registrar.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
