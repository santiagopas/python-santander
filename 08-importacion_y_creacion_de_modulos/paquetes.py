# Paquetes

""" 
Un paquete es una forma de organizar módulos relacionados en una estructura jerárquica de directorios. Los paquetes nos permiten agrupar módulos relacionados y evitar conflictos de nombres entre módulos.

 

Crear y utilizar paquetes
Para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado __init__.py dentro del directorio. Este archivo puede estar vacío o contener código de inicialización del paquete.

Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:

mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
Luego, podemos importar y utilizar los módulos del paquete en nuestro programa.

from mi_paquete import modulo1, modulo2


modulo1.funcion1()
modulo2.funcion2()
En este ejemplo, se importan los módulos modulo1 y modulo2 del paquete mi_paquete y se utilizan las funciones definidas en ellos.

La importación y creación de módulos y paquetes en Python nos permite organizar y reutilizar nuestro código de manera eficiente. Al modularizar nuestro código, podemos mantener un código más legible, estructurado y fácil de mantener.

Recuerda explorar la biblioteca estándar de Python y aprovechar los módulos existentes, que pueden facilitarte muchas tareas comunes. Además, no dudes en crear tus propios módulos y paquetes para organizar y reutilizar tu código de manera efectiva.
"""