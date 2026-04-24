# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from stack import Stack
from random import randint, choice

pila = Stack()

nombres = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Groot", "Rocket Raccoon", "Doctor Strange", "Captain Marvel", "Drax", "Gamora"]

for i in range(10):
    nombre = choice(nombres)
    peliculas = randint(1, 10)
    pila.push((nombre, peliculas))

pila.show()

print()

pila_aux = Stack()

pos = 1

pos_rocket = None
pos_groot = None
mas_de_5 = []
pelis_black_widow = None
iniciales = []

while pila.size() > 0:
    personaje = pila.pop()
    nombre = personaje[0]
    peliculas = personaje[1]

    if nombre == 'Rocket Raccoon':
        pos_rocket = pos

    if nombre == 'Groot':
        pos_groot = pos

    if peliculas > 5:
        mas_de_5.append((nombre, peliculas))

    if nombre == 'Black Widow':
        pelis_black_widow = peliculas

    if nombre[0] in ['C', 'D', 'G']:
        iniciales.append(nombre)

    pila_aux.push(personaje)
    pos += 1

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print('Resultados:')

if pos_rocket is not None:
    print('Rocket Raccoon está en la posición:', pos_rocket)
else:
    print('Rocket Raccoon no está en la pila')

if pos_groot is not None:
    print('Groot está en la posición:', pos_groot)
else:
    print('Groot no está en la pila')

print('Personajes que participaron en más de 5 películas:')
if len(mas_de_5) > 0:
    for nombre, peliculas in mas_de_5:
        print(nombre, "-", peliculas)
else:
    print('No hay personajes con más de 5 películas')

if pelis_black_widow is not None:
    print("Black Widow participó en:", pelis_black_widow, 'películas')
else:
    print('Black Widow no está en la pila')

print('Personajes que empiezan con C, D o G:')
if len(iniciales) > 0:
    for nombre in iniciales:
        print(nombre)
else:
    print('No hay personajes que cumplan la condición')