# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones: norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de partida, retornando por el mismo camino que fue.

from stack import Stack
from random import randint, choice

pila = Stack()

direcciones = ['norte', 'sur', 'este', 'oeste', 'noreste', 'noroeste', 'sureste', 'suroeste']

for i in range(10):
    pasos = randint(1,10)
    direccion = choice(direcciones)
    pila.push((pasos, direccion))

pila.show()

print()

pila_aux = Stack()

opuestas = {
    'norte': 'sur',
    'sur': 'norte',
    'este': 'oeste',
    'oeste': 'este',
    'noreste': 'suroeste',
    'noroeste': 'sureste',
    'sureste': 'noroeste',
    'suroeste': 'noreste'
}

while pila.size() > 0:
    pasos, direccion = pila.pop()
    pila_aux.push((pasos, opuestas[direccion]))

pila_aux.show()