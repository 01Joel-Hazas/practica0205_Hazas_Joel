# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

palabra = input("Introduce una palabra:")
vocales = [ 'a', 'e', 'i', 'o', 'u']

def num_vocales(palabra):
	for vocal in vocales:
		contador = 0
		for letra in palabra:
			if letra == vocal:
				contador += 1
		print("La vocal " + vocal + " aparece " + str(contador) + " veces")

print(str(num_vocales(palabra)))