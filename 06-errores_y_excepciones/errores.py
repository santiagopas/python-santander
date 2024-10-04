# Manejo de errores y excepciones

#Cuando escribimos programas, es común encontrarnos con situaciones inesperadas o errores durante la ejecución. Python proporciona un mecanismo para manejar estos errores de manera controlada utilizando el manejo de excepciones. Esto nos permite capturar y manejar errores específicos sin que el programa se detenga abruptamente.

# Error de sintaxis (SyntaxError)
# Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle.
def mi_funcion() # Falta los dos puntos
    print("Hola")
    
# Error de nombre (NameError)
# Ocurre cuando se hace referencia a una variable o función que no ha sido definida.

print(variable_no_definida)

# Error de tipo (TypeError)
# Ocurre cuando se realiza una operación con tipos de datos incompatibles, como intentar sumar un número y una cadena.
resultado = 5 + "10"
 

# Error de índice (IndexError)
# Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia.
lista = [1, 2, 3]
print(lista[3])  # El índice 3 está fuera del rango
 

# Estos son solo algunos ejemplos de errores comunes. Cuando ocurre un error, Python genera una excepción y muestra un mensaje de error que incluye el tipo de excepción y una descripción del problema.