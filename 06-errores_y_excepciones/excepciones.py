# Manejo de excepciones

# En Python, las excepciones son errores que ocurren durante la ejecución de un programa. Cuando ocurre una excepción, el programa se detiene y genera un mensaje de error que indica el tipo de excepción y la causa del error.

# El manejo de excepciones nos permite capturar y manejar errores de manera controlada utilizando las declaraciones try, except y opcionalmente finally.

try:
    # Código que puede generar una excepción
    resultado = 5 / 0
except ZeroDivisionError:
    # Manejo de la excepción
    print("Error: División por cero")
# En este ejemplo, el código dentro del bloque try genera una excepción ZeroDivisionError al intentar dividir un número por cero. La excepción se captura y se maneja en el bloque except, que imprime un mensaje de error indicando que se ha producido una división por cero.

# También es posible manejar múltiples excepciones utilizando varias cláusulas except:
# El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except NameError:
    print("Error: Variable no definida")
except ValueError:
    print("Error: Valor inválido")

# En este ejemplo, se intenta dividir un número por cero, lo que genera una excepción ZeroDivisionError. La excepción se captura y se maneja en el primer bloque except. Si se produce una excepción NameError o ValueError, se capturan y manejan en los bloques except correspondientes.

# Finally
# El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.

try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()

# En este ejemplo, se intenta abrir un archivo para lectura. Si el archivo no se encuentra, se captura la excepción FileNotFoundError y se imprime un mensaje de error. Luego, el bloque finally se ejecuta para cerrar el archivo, independientemente de si se produjo una excepción o no.

# Excepciones personalizadas

"""Además de las excepciones incorporadas en Python, también puedes crear tus propias excepciones personalizadas. Esto es útil cuando deseas manejar situaciones específicas de tu programa.

Para crear una excepción personalizada, debes crear una clase que herede de la clase base Exception o de una de sus subclases. Luego, puedes lanzar la excepción utilizando la palabra clave raise."""


def funcion():
    condicion = True
    if condicion:
        raise Exception("Mensaje de error")


try:
    funcion()
except Exception as e:
    print("Error:", e)

"""En este ejemplo, se define una función llamada funcion(). Dentro de la función, se verifica una condición y, si se cumple, se genera una excepción utilizando la declaración raise. En lugar de crear una clase personalizada, se utiliza directamente la clase base Exception para generar la excepción.

Luego, se utiliza un bloque try-except para capturar y manejar la excepción. La variable e se utiliza para acceder a la descripción del error proporcionada al generar la excepción.

El manejo de errores y excepciones es una parte fundamental de la programación en Python. Te permite manejar situaciones inesperadas de manera controlada y evitar que tu programa se bloquee o se detenga abruptamente.

Cuando ocurre un error en tu código, Python genera una excepción. Al utilizar bloques try-except, puedes capturar y manejar estas excepciones de manera adecuada. Puedes especificar diferentes bloques except para manejar distintos tipos de excepciones y realizar acciones específicas en cada caso.

Además, el bloque finally te permite ejecutar código de limpieza o liberación de recursos, independientemente de si ocurrió una excepción o no. Esto es útil para garantizar que ciertas acciones se realicen siempre, como cerrar archivos o conexiones de base de datos.

Considera los posibles errores que pueden ocurrir en tu código y utiliza el manejo de excepciones adecuado para manejarlos de manera apropiada. Esto hará que tus programas sean más robustos y confiables.
 
"""