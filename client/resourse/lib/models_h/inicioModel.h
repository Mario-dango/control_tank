#ifndef INICIOMODEL_H
#define INICIOMODEL_H

#include <QString>

class InicioModel
{
public:
    InicioModel();
    
    QString nombreUsuario() const;
    void setNombreUsuario(const QString &nombreUsuario);

    QString contrasena() const;
    void setContrasena(const QString &contrasena);

    bool credencialesValidas() const;

private:
    QString m_nombreUsuario;
    QString m_contrasena;
};

#endif // INICIOMODEL_H
