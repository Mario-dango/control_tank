#ifndef DASHBOARD_MODEL_H
#define DASHBOAR_DMODEL_H

#include <QObject>

class DashboardModel : public QObject
{
    Q_OBJECT

public:
    explicit DashboardModel(QObject *parent = nullptr);

    // Métodos para actualizar y consultar datos del panel principal
    void updateData();
    int getNumberOfItems();
    QString getItemName(int index);

private:
    // Datos del panel principal
    int m_numberOfItems;
    QVector<QString> m_itemNames;
};

#endif // DASHBOARDMODEL_H
