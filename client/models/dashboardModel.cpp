#include "../client/resourse/lib/models_h/dashboardMode.h"

DashboardModel::DashboardModel(QObject *parent)
    : QObject(parent)
{
    // Inicialización de datos del panel principal
    m_numberOfItems = 0;
}

void DashboardModel::updateData()
{
    // Carga de datos del panel principal desde alguna fuente (por ejemplo, una base de datos)
    m_numberOfItems = 5;
    m_itemNames = QVector<QString>{"Item 1", "Item 2", "Item 3", "Item 4", "Item 5"};
}

int DashboardModel::getNumberOfItems()
{
    return m_numberOfItems;
}

QString DashboardModel::getItemName(int index)
{
    if (index >= 0 && index < m_itemNames.size()) {
        return m_itemNames[index];
    } else {
        return "";
    }
}
