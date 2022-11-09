# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota
# que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
asignaturasRecuperar = []
for asignatura in asignaturas:
    notaObtenida = float(input("Introduce que nota has sacado en " + asignatura + ":"))
    if notaObtenida < 5:
        asignaturasRecuperar.append(asignatura)

print("Debes recuperar:")
for asignaturaSuspensa in asignaturasRecuperar:
    print(asignaturaSuspensa, end=", ")
