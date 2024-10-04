# Importacion y creacion de modulos

# En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas. La importación de módulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.

"""
Ten en cuenta
Python viene con una amplia biblioteca estándar de módulos que proporcionan funcionalidades adicionales. Estos módulos están disponibles sin necesidad de instalarlos por separado.
"""

# ? Importar módulos
# Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. Podemos importar un módulo completo o funciones específicas de un módulo.


"""En este ejemplo, se importa el módulo math utilizando la declaración import. Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.

También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función. 
"""
from math import sqrt

resultado = sqrt(25)

print(resultado)  # 5.0

# en este caso, se importa la función sqrt() del módulo math directamente, lo que nos permite utilizar la función sin tener que especificar el nombre del módulo.

# ? Funciones y clases de módulos estándar
# La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles. Algunos ejemplos comunes incluyen:

# Math: Proporciona funciones matemáticas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.
# Random: Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.
# Datetime: Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

fecha_actual = datetime.datetime.now()
dia_actual = fecha_actual.day
print(f"Fecha actual: {fecha_actual}, día: {dia_actual}")


import mi_modulo
print(mi_modulo.saludar("Juan"))

# ! Organización del código en módulos
"""A medida que nuestros programas crecen en tamaño y complejidad, es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.

Por ejemplo, podemos tener un módulo operaciones.py que contenga funciones relacionadas con operaciones matemáticas, y otro módulo utilidades.py que contenga funciones de uso general. De esta manera, podemos importar y utilizar las funciones específicas que necesitamos en cada parte de nuestro programa."""

