# Funciones

"""Las funciones son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario. Las funciones nos ayudan a organizar nuestro código, evitar la repetición y hacer que nuestros programas sean más modulares y fáciles de mantener.
"""
# Definición y llamada de funciones
"""Para definir una función en Python, utilizamos la palabra clave def seguida del nombre de la función y paréntesis. Opcionalmente, podemos especificar parámetros dentro de los paréntesis. El bloque de código de la función se indenta después de los dos puntos.

Para llamar a una función, simplemente escribimos el nombre de la función seguido de paréntesis:"""


def saludo(nombre):
    print("Hola mundo!", nombre)


saludo("parametros de la funcion")

# Parámetros y argumentos
# Las funciones pueden aceptar parámetros, que son valores que se pasan a la función cuando se la llama. Los parámetros se especifican dentro de los paréntesis en la definición de la función.


def dias_de_la_semana(dia):
    print("Hoy es", dia)


dias_de_la_semana("viernes")

# Valores de retorno
"""Las funciones pueden devolver valores utilizando la palabra clave return. El valor de retorno puede ser utilizado por el código que llama a la función."""


def suma(a, b):
    return a + b


resultado = suma(2, 3)
print(resultado)

# Funciones anónimas (lambda)
"""Python permite crear funciones anónimas o funciones lambda, que son funciones sin nombre definidas en una sola línea. Se utilizan comúnmente para funciones pequeñas y concisas.
"""


def cuadrado(x): return x ** 2


print(cuadrado(5))

# Alcance de las variables (local vs. global)
"""Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo son accesibles dentro de la función. Por otro lado, las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del programa."""


def funcion():
    variable_local = 10
    print(variable_local)


variable_global = 20


def funcion2():
    print(variable_global)


funcion()
funcion2()
print(variable_global)
# print(variable_local)  # Error

"""Documentación de funciones (docstrings)
Es una buena práctica documentar nuestras funciones utilizando docstrings. Los docstrings son cadenas de texto que describen el propósito, los parámetros y el valor de retorno de una función. Se colocan inmediatamente después de la definición de la función y se encierran entre triples comillas dobles."""


def area_rectangulo(base, altura):
    """ Args:
         base(float): La base del rectángulo.
         altura(float): La altura del rectángulo.
         Returns:
         float: El área del rectángulo
         """
    return base * altura


resultado_area = area_rectangulo(5.9, 10)
print(resultado_area)

"""Funciones con número variable de argumentos
Python permite definir funciones que acepten un número variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro."""
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        return total
print(suma_variable(2, 3, 4))
print(suma_variable(3, 4, 5, 6))

"""Las funciones son una herramienta fundamental en la programación y nos permiten estructurar y modularizar nuestro código. Con la capacidad de definir funciones personalizadas, podemos encapsular tareas específicas y reutilizarlas en diferentes partes de nuestro programa.

Además de las funciones definidas por el usuario, Python también proporciona una amplia gama de funciones incorporadas que podemos utilizar directamente, como print(), len(), range(), entre otras."""