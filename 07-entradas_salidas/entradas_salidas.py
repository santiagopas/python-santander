# Entradas/salidas

# En Python, la entrada y salida de datos nos permite interactuar con el usuario y manipular archivos. Podemos solicitar información al usuario, mostrar resultados en la pantalla y leer o escribir datos en archivos externos.

 

# Entrada de datos del usuario
# Para obtener información del usuario durante la ejecución del programa, podemos utilizar la función input(). Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese un valor.

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("Hola,", nombre, "tienes", edad, "años.")

# En este ejemplo, la función input() muestra el mensaje "Ingrese su nombre:" y espera a que el usuario ingrese un valor. El valor ingresado por el usuario se almacena en la variable nombre y se imprime en la pantalla.

#TODO:Importante
# La función input() siempre devuelve una cadena de texto. Si deseas trabajar con otros tipos de datos, como números enteros o flotantes, debes realizar una conversión explícita utilizando funciones como int() o float().

#  Salida de datos
# Para mostrar información en la pantalla, utilizamos la función print(). Esta función toma uno o más argumentos y los muestra en la consola.
# Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.

nombre = "Juan"
edad = 25

print(f"Hola, {nombre}. Tienes {edad} años.")