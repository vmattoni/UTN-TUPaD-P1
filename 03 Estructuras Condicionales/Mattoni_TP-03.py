# EJERCICIOS TP 3 DE PROGRAMACIÓN 1

# 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else: 
    print("Adulto/a")

# 5
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6
from statistics import mode, median, mean  
import random  
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

# 7
string = input("Ingresa una palabra o frase: ")
if string and string[-1].lower() in 'aeiouáéíóúü':
    string += '!'
print(string)

# 8
nombre = input("Ingresa tu nombre: ")
opcion = input("Elige una opción:\n1- Nombre en mayúsculas\n2- Nombre en minúsculas\n3- Nombre con la primera letra mayúscula\n")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else: 
    print("Debes elegir una opción válida.")

# 9
dato = float(input("¿Cuál fue la magnitud del terremoto?: "))

if dato < 3:
    print("Muy leve (imperceptible)")
elif dato >= 3 and dato < 4:
    print("Leve (ligeramente perceptible)")
elif dato >= 4 and dato < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif dato >= 5 and dato < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif dato >= 6 and dato < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10
hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

if hemisferio != 'N' and hemisferio != 'S':
    print("Error: Hemisferio no válido. Debe ser N o S.")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == 'N' else "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == 'N' else "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == 'N' else "Invierno"
    else:
        estacion = "Otoño" if hemisferio == 'N' else "Primavera"
    
    print(f"Estación actual: {estacion}")
