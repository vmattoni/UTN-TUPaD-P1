# EJERCICIOS TP 5 DE PROGRAMACIÓN 1

# 1
multiplos_4 = list(range(4, 101, 4))
print(multiplos_4)

# 2
mi_lista = ["manzana", "banana", "naranja", "uva", "pera"]
print(mi_lista[-2])

# 3
lista_vacia = []
lista_vacia.append("Python")
lista_vacia.append("Java")
lista_vacia.append("C++")
print(lista_vacia)

# 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"    # Segundo elemento (índice 1)
animales[-1] = "oso"    # Último elemento (índice -1)
print(animales)

# 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# 6
numeros = list(range(10, 31, 5))
print(numeros[:2])

# 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["corolla", "hilux"]
print(autos)

# 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# 10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)
