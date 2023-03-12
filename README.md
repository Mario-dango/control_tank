# control_tank

Repositorio creado para mostrar el proyecto de control de un robot móvil con una estructura de servidor cliente para la materia de Programación Orientada a Objetos de la facultad de ingeniería de la UNCuyo.

## Contenido
En el presente repositorio posee 7 elementos de los cuales 5 son carpetas, las cuales se detallan a continuación:
- .vscode Es la carpeta de configuraciones que se usaron para el desarrollo del proyecto, ya que el mismo fue realizado dentro del entorno y haciendo uso de las herramientas y extensiones de Visual Studio Code.
- client Es la carpeta en donde se encuenta un cliente en c++ sin terminar que incluye interfaz gráfica QT, el mismo se dejó de lado ya que se propuso llegar con los plazos de tiempo implementando en el lado del cliente una interfaz estilo consola.
- client_cmd Es la carpeta contenedora de la aplicación cliente en c++ del proyecto, actualmente funcional y operativa con algunos pequeños bugs.
- informe Es la carpeta que contiene los diagramas y el documento que recopila todo acerca del presente proyecto (control tank).
- server Por último la carpeta contenedora de la aplicación del servidor, hecha en python y es la encargada de conectarse directamente con el robot móvil y de establecer comunicación con el cliente ambos bajo protocolo XmlRpc.
