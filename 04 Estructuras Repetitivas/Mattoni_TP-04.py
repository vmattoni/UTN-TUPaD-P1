# EJERCICIOS TP 4 DE PROGRAMACIÓN 1

# 1
for i in range(101):
print(i)

# 2
numero = input("Ingrese un número entero: ")
print(f"El número tiene {len(numero)} dígitos")

# 3
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0

if inicio > fin:
inicio, fin = fin, inicio

for i in range(inicio + 1, fin):
suma += i

print(f"La suma es: {suma}")

# 4
total = 0
while True:
num = int(input("Ingrese un número (0 para terminar): "))
if num == 0:
break
total += num
print(f"Total acumulado: {total}")

# 5
import random
numero_secreto = random.randint(0, 9)
intentos = 0

while True:
intento = int(input("Adivina el número (0-9): "))
intentos += 1
if intento == numero_secreto:
print(f"¡Correcto! Lo lograste en {intentos} intentos")
break
print("Intenta nuevamente")

# 6
for i in range(100, -1, -2):
print(i)

# 7
numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(numero + 1):
suma += i

print(f"La suma es: {suma}")

# 8
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(100): # Cambiar a 5 para pruebas
num = int(input("Ingrese un número entero: "))
if num % 2 == 0:
pares += 1
else:
impares += 1
if num > 0:
positivos += 1
elif num < 0:
negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9
suma = 0
for _ in range(100): # Cambiar a 5 para pruebas
num = int(input("Ingrese un número entero: "))
suma += num

media = suma / 100 # Cambiar denominador según cantidad usada
print(f"La media es: {media}")

# 10
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print(f"Número invertido: {invertido}")
