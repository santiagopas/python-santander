# Diccionarios
"""Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. Los diccionarios se encierran entre llaves {}, y los pares clave-valor se separan por comas."""

# Creación y acceso a un diccionario

"""Para crear un diccionario, utiliza llaves y separa las claves y valores con dos puntos.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:
También puedes utilizar el método get() para obtener el valor de una clave. Si la clave no existe, devuelve un valor predeterminado (por defecto, None).
"""

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print("----------------Diccionarios----------------")

print(persona["nombre"])  # Imprime: Juan
print(persona["edad"])  # Imprime: 25
print(persona["ciudad"])  # Imprime: Madrid
print(persona.get("nombre"))  # Imprime: Juan

# Métodos de diccionarios

"""Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario."""

print("----------------Métodos de diccionarios----------------")

print(persona.keys())  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values())  # Salida: dict_values(['Juan', 25, 'Madrid'])
# Salida: dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Madrid')])
print(persona.items())
# Actualiza el diccionario con nuevos valores, la consola no imprime nada o None
print(persona.update({"nombre": "Pedro", "edad": 30}))
print(persona)  # Salida: {'nombre': 'Pedro', 'edad': 30, 'ciudad': 'Madrid'}
print(persona.update({"profesion": "Ingeniero"}))
print(persona)
