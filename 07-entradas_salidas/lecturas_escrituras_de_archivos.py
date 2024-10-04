# Lectura y escritura de archivos

#  Python nos permite leer y escribir datos en archivos externos. Podemos abrir archivos en diferentes modos, como lectura ("r"), escritura ("w") o anexar ("a"), y realizar operaciones de lectura y escritura.Lectura de archivos
# Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().

archivo = open("07-entradas_salidas/archivo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# Escritura de archivos
# Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.

archivo = open("07-entradas_salidas/archivo.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()
# archivo.write("Hola, mundo!")  # Se sobrescribe el contenido anterior\
    
#!	Importante
# Es importante cerrar siempre los archivos después de utilizarlos para liberar los recursos del sistema. 

#  También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática. Esto garantiza que el archivo se cierre correctamente al finalizar el bloque de código.

with open("07-entradas_salidas/archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    
"""La entrada y salida de datos en Python nos brinda una gran flexibilidad para interactuar con el usuario y manipular archivos externos. Podemos solicitar información al usuario, mostrar resultados en la pantalla y leer o escribir datos en archivos de texto. Recuerda siempre manejar adecuadamente la apertura y cierre de archivos, y considerar las posibles excepciones que pueden ocurrir durante las operaciones de entrada/salida."""