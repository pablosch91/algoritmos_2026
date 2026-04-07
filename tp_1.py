#TRABAJO PRÁCTICO Nº1: RECURSIVIDAD 

# RECURSIVIDAD: está representada mediante función que tiene que cumplir dos condiciones: 
# - tener al menos una condición clara de fin para poder en algún momento salir
# - se debe poder llamar a sí misma dentro de la función (llamada recursiva o autollamada), "el problema pasa a ser parte de la solución"
# mientras la función se llama a sí misma, queda una parte en memoria sin resolver hasta que llegue a la condición de fin

# 5. Desarrollar una función que permita convertir un número romano en un número decimal.

valores = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romano_a_decimal(num):
  if num == '':
    return 0
  elif len(num) == 1:
    return valores[num]
  else:
    if valores[num[0]] >= valores[num[1]]: #XIII
      return valores[num[0]] + romano_a_decimal(num[1:])
    elif valores[num[0]] < valores[num[1]]: #XLII
      return valores[num[1]] - valores[num[0]] + romano_a_decimal(num[2:])

print(romano_a_decimal('XLII'))

# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

#mochila = ['comida', 'mapa', 'sable de luz', 'ropa']
mochila = ['comida', 'mapa', 'ropa']

def usar_la_fuerza(i):
  if i >= len(mochila):
    return None
  elif mochila[i] == 'sable de luz':
    return True, i #sale en forma de tupla
  else:
    return usar_la_fuerza(i+1)

if usar_la_fuerza(0): # if usar_la_fuerza(0) == True:
    print(f'La mochila contiene un sable de luz y se sacaron {usar_la_fuerza(0)[1]} objetos')
else:
    print('No se encontró un sable de luz')