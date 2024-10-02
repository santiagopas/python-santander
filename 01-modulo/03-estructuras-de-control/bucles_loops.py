# Bucles/loops

# Los bucles nos permiten repetir un bloque de código varias veces. En Python, los bucles más comunes son for y while.

# FOR
# El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. La sintaxis básica es la siguiente:
# una tupla es una secuencia de elementos que no se pueden modificar, es decir, son inmutables. Se definen utilizando paréntesis y separando los elementos por comas. Por ejemplo: tupla = (1, 2, 3)

# una lista es una secuencia de elementos que se pueden modificar, es decir, son mutables. Se definen utilizando corchetes y separando los elementos por comas. Por ejemplo: lista = [1, 2, 3]

# una cadena es una secuencia de caracteres. Se definen utilizando comillas simples ('...') o dobles ("..."). Por ejemplo: cadena = "Hola, mundo!"

print("----------------Bucle for----------------")

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

print("----------------Bucle for in range----------------")

print("Números del 1 al 5 multiplicados por 2")

for numero in range(1, 6):
    print(numero * 2)

# En este ejemplo, el bucle for itera sobre la lista frutas. En cada iteración, la variable fruta toma el valor de un elemento de la lista, y se ejecuta el bloque de código dentro del bucle. En este caso, se imprime cada fruta en una línea separada

# WHILE
# El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:

print("----------------Bucle while----------------")

contador = 0

while contador < 5:
    print(contador)
    contador += 1

# En este ejemplo, el bucle while se ejecuta mientras la variable contador sea menor que 5. En cada iteración, se imprime el valor de contador y luego se incrementa en 1 mediante la instrucción contador += 1. El bucle se detendrá cuando contador alcance el valor de 5.

# Es importante tener cuidado al usar el bucle while, ya que, si la condición nunca se vuelve falsa, el bucle se ejecutará indefinidamente, lo que se conoce como un bucle infinito.


# Control de bucles
# Python proporciona algunas instrucciones especiales para controlar el flujo de ejecución dentro de los bucles:

# break: La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición. Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.

print("----------------Bucle while con BREAK----------------")

contador = 0

while True:
    print(contador)
    contador += 1

    if contador == 5:
        break

print("----------------FOR Continue----------------")

# Continue: La instrucción continue se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.

i = 0
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# En este ejemplo, el bucle for itera sobre los números del 0 al 9 utilizando la función range(). Dentro del bucle, se verifica si el número es divisible por 2 utilizando el operador de módulo %. Si el número es divisible por 2 (es decir, si es par), se ejecuta la instrucción continue, lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle. Como resultado, solo se imprimirán los números impares.

print("----------------FOR Pas----------------")

# Pass: La instrucción pass es una operación nula que no hace nada. Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción. Por ejemplo:

for i in range(5):
	pass

# En este ejemplo, el bucle for itera sobre los números del 0 al 4, pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass. Esto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.

# Conclusión
# Las estructuras de control son herramientas poderosas que nos permiten controlar el flujo de ejecución de nuestros programas. Con las estructuras condicionales (if, if-else, if-elif-else) podemos tomar decisiones basadas en condiciones, mientras que con los bucles (for, while) podemos repetir bloques de código varias veces. Además, las instrucciones break, continue y pass nos brindan un control adicional sobre el comportamiento de los bucles. Al combinar estas estructuras de control, podemos crear programas complejos y eficientes que realicen tareas específicas de manera automatizada.