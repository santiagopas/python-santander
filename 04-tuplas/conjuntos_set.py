# Conjuntos (set)

# Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos. Los conjuntos se encierran entre llaves {} o se crean utilizando la función set(). Los elementos de un conjunto se separan por comas.

# Creación y operaciones básicas

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

"""Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^)."""


print("----------------Conjuntos----------------")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
# Imprime {1, 2, 3, 4, 5} el numero 3 se repite en ambos conjuntos, pero en el resultado solo aparece una vez porque los conjuntos no admiten elementos duplicados
print(union)

insterseccion = conjunto1 & conjunto2
# Imprime {3} solo el numero 3 esta en ambos conjuntos
print(insterseccion)

diferencia = conjunto1 - conjunto2
# Imprime {1, 2} los numeros que estan en el conjunto1 pero no en el conjunto2
print(diferencia)

diferencia_simetrica = conjunto1 ^ conjunto2
# Imprime {1, 2, 4, 5} los numeros que estan en el conjunto1 y conjunto2 pero no en ambos
print(diferencia_simetrica)


# Métodos de conjuntos

print("----------------Métodos de conjuntos----------------")

"""
Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

add(elemento): agrega un elemento al conjunto.
remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
clear(): elimina todos los elementos del conjunto.
"""

conjunto2.add(6)
print(conjunto2)  # Salida: {3, 4, 5, 6}
frutas.add("pera")  # Agrega la fruta "pera" al conjunto frutas
print(frutas)
frutas.remove("banana")  # Elimina la fruta "banana" del conjunto frutas
print(frutas)
# No hace nada porque la fruta "uva" no está en el conjunto frutas
frutas.discard("uva")
print(frutas)
frutas.discard("pera")  # Elimina la fruta "pera" del conjunto frutas
print(frutas)
frutas.clear()  # Elimina todos los elementos del conjunto frutas
print(frutas)  # Salida: set() porque el conjunto frutas está vacío