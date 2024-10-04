# Tuplas

# Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. Los elementos de una tupla se encierran entre paréntesis (), separados por comas.

# Creación y acceso a una tupla

punto = (3, 4)

print(punto[0])  # Imprime: 3
print(punto[1])  # Imprime: 4

# A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. No se pueden agregar, eliminar o cambiar elementos en una tupla existente. Las tuplas son útiles cuando necesitas almacenar una colección de elementos que no deben modificarse, como coordenadas o datos de configuración.

# Métodos de las tuplas

"""
Métodos de tuplas en Python ( count, index, len )
Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
"""

mi_tupla = (1, 2, 3, 2, 4, 2)

print(mi_tupla.index(2))  # Saslida: 1
print(mi_tupla.index(2, 2))  # Salida: 3
# Salida: 3 aqui se especifica el inicio y fin de la busqueda, en este caso se busca el 2 en la posicion 2 y 4, el resultado es 3 porque el 2 esta en la posicion 3
print(mi_tupla.index(2, 2, 4))

print(mi_tupla.count(2))  # Salida: 3 (el 2 aparece 3 veces en la tupla)

print(len(mi_tupla))  # Salida: 6 (la tupla tiene 6 elementos)
