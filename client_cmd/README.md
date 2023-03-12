# Cliente CMD

En está carpeta se encuentra el cliente actualmente funcional que posee cómo interfaz de intreracción una consola parecida a la terminal, en la cual muestra un menú en donde se pueden seleccionar las opciones que se deseen. Actualmente se encuentra operativo al correr el archivo cmdCliente y el mismo tiene cómo parámetros de conexión al localhost (127.0.0.1) con el puerto número 8891.
En el cliente posee las siguiente funcionalidades:
- Conectar por bluetooth desde el servidor al robot móvil.
- Controlar de forma remota al robot movil ejecutando las siguientes acciones:
- - Deshabilitar/Habilitar motores.
- - Mover hacia adelante.
- - Mover hacia atrás.
- - Girar a la derecha.
- - Girar a la izquierda.
- - Detener el movimiento actual.
- También permite visualizar y cambiar parámetros de conexión al servidor XmlRpc.
- Solicitar el registro de actividades del robot en un archivo de formato xml.
- Visualizar en la consola o terminal el contenido del archivo xml.

## Compilar
Para poder modificar y retocar el proyecto se puede luego compilar corriendo el archivo makefile dentro del presente directorio, allí están todas las dependencias que se necesitaron para la correcta compilación del proyecto cliente_cmd.
