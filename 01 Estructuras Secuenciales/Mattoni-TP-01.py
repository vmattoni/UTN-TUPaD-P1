# 1 -------------

print("Hola mundo!")

# 2 -------------

nombre = input("¿Podrías decirme cuál es tu nombre? ")
print(f"Un placer {nombre}! Gusto en conocerte! ")

# 3 -------------

nombre = input(" Perdona que te pregunte de nuevo, pero ¿podrías decirme cuál es tu nombre de nuevo? ")
apellido = input("¡Excelente! ¿Y cuál es tu apellido? ")
edad = input("¿Cuántos años tenés? ")
nacionalidad = input("Y por ultimo, ¿De dónde sos? ")

print(f"Según los datos que me haz proporcionado, si te fueses a presentar dirías: Soy {nombre} {apellido}, tengo {edad} y soy de {nacionalidad}")

# 4 -------------

radio = int(input("Porfavor indicame el radio de un circulo para calcular su área y perímetro. "))

area = 3.1416 * (radio * radio)
perimetro = (radio * 2) * 3.1416

print(f"Su circulo con radio = {radio} tiene un area de {area} y un perimetro de {perimetro}")

# 5 -------------

seg = int(input("Indicame una cantidad de segundos para convertirlos en su equivalente en horas. "))

hora = ((seg / 60) / 60)
hora_redondeada = round(hora, 2)

print(f"La cantidad de segundos que usted ingresó, {seg}, equivalen a {hora_redondeada} horas.")

# 6 -------------

num = int(input("Indicame un número para mostrar su tabla de multiplicar del 1 al 10. "))

tabla1 = num * 1
tabla2 = num * 2
tabla3 = num * 3
tabla4 = num * 4
tabla5 = num * 5
tabla6 = num * 6
tabla7 = num * 7
tabla8 = num * 8
tabla9 = num * 9
tabla10 = num * 10

print(f"{num} * 1 = {tabla1}\n{num} * 2 = {tabla2}\n{num} * 3 = {tabla3}\n{num} * 4 = {tabla4}\n{num} * 5 = {tabla5}\n{num} * 6 = {tabla6}\n{num} * 7 = {tabla7}\n{num} * 8 = {tabla8}\n{num} * 9 = {tabla9}\n{num} * 10 = {tabla10}")

# 7 -------------

num1 = int(input("Ahora necesito que me indique dos números para conocer su suma, resta, multiplicación y división.\nDame el primer número. "))
num2 = int(input("Dame el segundo número. "))

suma = num1 + num2
div = num1 / num2
mult = num1 * num2
resta = num1 - num2

print(f"{num1} + {num2} = {suma}\n{num1} / {num2} = {div}\n{num1} * {num2} = {mult}\n{num1} - {num2} = {resta}\n")

# 8 -------------

altura = float(input("Indicame tu altura en metros (Ejemplo: 1.66). "))
peso = int(input("Indicame tu peso en kilogramos (Ejemplo:). "))

imc = round(peso / (altura ** 2), 2)


print(f"Muchas gracias! Según los datos ingresados tu IMC es: {imc}")

# 9 -------------

print(f"Ahora necesito que me de una temperatura en grados celcius para transformarla en farenheit.")

celsius = int(input("Escriba los grados celcius. "))
farenheit = (celsius * 9/5) + 32

print(f"La cantidad de {celsius} grados celsius equivalen a {farenheit} grados farenheit.")

# 10 -------------

print(f"Como último, necestiaré que me de 3 números para sacar un promedio.")

num1 = int(input("Ingrese el primer número. "))
num2 = int(input("Ingrese el segundo número. "))
num3 = int(input("Ingrese el tercer número. "))

promedio = (num1 + num2 + num3) / 3

print(f"Listo! El promedio de los tres números ingresados es: {promedio}")
print(f"Eso sería todo, muchas gracias por participar!")
