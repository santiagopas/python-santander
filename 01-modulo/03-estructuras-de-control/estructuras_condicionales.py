# Estructuras de control

# Estructuras condicionales
# Las estructuras condicionales nos permiten ejecutar diferentes bloques de código según se cumpla o no una determinada condición. En Python, las estructuras condicionales más utilizadas son if, if-else y if-elif-else.

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

# En este ejemplo, la condición edad >= 18 se evalúa como True, por lo que se ejecuta el bloque de código dentro del if y se imprime el mensaje "Eres mayor de edad".

# IF ELSE

# La estructura if-else nos permite especificar un bloque de código alternativo que se ejecutará si la condición del if es falsa. La sintaxis básica es la siguiente:

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad." De lo contrario, se ejecutará el bloque de código dentro del else y se imprimirá el mensaje "Eres menor de edad."

# IF ELIF ELSE
# La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente:

calificacion = 85

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("Muy bueno")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necessita mejorar")
