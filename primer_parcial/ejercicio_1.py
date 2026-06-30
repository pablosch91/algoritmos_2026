# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

list_heroes = [
    "Superman",
    "Batman",
    "Mujer Maravilla",
    "Flash",
    "Linterna Verde",
    "Aquaman",
    "Spider-Man",
    "Iron Man",
    "Capitán América",
    "Thor",
    "Hulk",
    "Black Panther",
    "Doctor Strange",
    "Wolverine",
    "Capitana Marvel"
]

def buscar(lista, buscado, posicion):
    if posicion == len(lista):
        return -1

    elif lista[posicion] == buscado:
        return posicion

    else:
        return buscar(lista, buscado, posicion + 1)

pos = buscar(list_heroes, "Capitán América", 0)

if pos != -1:
    print("Encontrado en la posición", pos)
else:
    print("No se encontró")

def listar(lista, posicion):
    if posicion == len(lista):
        return None
    else:
        print(lista[posicion])
        return listar(lista, posicion + 1)
    
print()
listar(list_heroes, 0)