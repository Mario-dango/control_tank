#include "../resourse/lib/models_h/inicioModel.h"

InicioModel::InicioModel()
{
}

QString InicioModel::nombreUsuario() const
{
    return m_nombreUsuario;
}

void InicioModel::setNombreUsuario(const QString &nombreUsuario)
{
    m_nombreUsuario = nombreUsuario;
}

QString InicioModel::contrasena() const
{
    return m_contrasena;
}

void InicioModel::setContrasena(const QString &contrasena)
{
    m_contrasena = contrasena;
}

bool InicioModel::credencialesValidas() const
{
    // Comprobar si las credenciales son válidas
    return (m_nombreUsuario == "admin" && m_contrasena == "admin");
}

