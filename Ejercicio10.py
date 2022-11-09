# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
# y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22 , 80, 65 , 8]
precios.sort();
precioMax = 0;
precioMin = precios[0];

for precio in precios:
    if precio > precioMax:
        precioMax = precio;

print("El mínimo es " + str(precioMin))
print("El máximo es " + str(precioMax))
