SETUP // CONFIGURACIÓN
1. Si ya tienes python instalado en tu computadora pasa al paso numero 3.
2.Instala pyton 2.7 desde el siguiente enlace https://www.python.org/download/releases/2.7/
3.Dependiendo del sistema windows que tengas revisa lo siguiente*
Windows  10 / 8
Presiona la tecla de Windows y en el buscador escribe "Editar las variables del entorno de esta cuenta"
En la ventana que aparece busca en la parte inferior derecha un boton que dice "Variables de entorno..."
En la ventana Editar selecciona el boton de "Nuevo" y escribe la ruta en la que instalaste python*
Haga click en aceptar.

Windows 7
Desde el escritorio, haga clic con el botón derecho del mouse en el icono de la computadora.
Seleccione Propiedades en el menú contextual.
Haga clic en el enlace Configuración avanzada del sistema.
Haga clic en Variables de entorno. En la sección Variables del sistema, busque la variable de entorno PATH y selecciónela. 
Haga clic en Editar. Si no existe la variable de entorno PATH, haga clic en Nuevo.
En la ventana Editar la variable del sistema (o Nueva variable del sistema), debe especificar el valor de la variable de entorno PATH.
Haga clic en Aceptar.

*En la instalacion normal de python se debería de hacer este proceso automaticamente.

4. Instala git desde la siguiente dirección : https://git-scm.com/download/win
5. Presion Windos+R y escribe "cmd" y presiona la tecla de Enter.
6. Dentro de la terminal escribe escribe lo siguiente: pip install git+git://github.com/shotgunsoftware/python-api.git
7. Presiona enter para que comience el comando y una vez finalizado cierra la terminal.
8. Ve a la carpeta donde descargaste el archivo asset_management.py
9.Manten presionada la tecla Shift y en cualquier parte de la ventana presion el boton derecho del ratón.
10.Selecciona la opcion que dice "Abrir ventana de comandos aqui" y escribe asset_management.py -h para ver la ayuda del script.
