# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Introduce una palabra:")
def palindromo(palabra):
    if str(palabra) == str(palabra)[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
print(palindromo(palabra))