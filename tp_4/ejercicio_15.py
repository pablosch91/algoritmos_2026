# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
# o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

from list_ import List

class Pokemon:
 
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
 
    def __str__(self):
        return f'Nombre: {self.nombre} - Nivel: {self.nivel} - Tipo: {self.tipo} - Subtipo: {self.subtipo}'

class Entrenador:
 
    def __init__(self, nombre, torneos_ganados, batallas_ganadas, batallas_perdidas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
        self.pokemons = List()  # lista de lista: cada entrenador tiene su propia List de Pokemon
 
    def __str__(self):
        return (f'{self.nombre} - Torneos ganados: {self.torneos_ganados} - '
                f'Batallas ganadas: {self.batallas_ganadas} - Batallas perdidas: {self.batallas_perdidas}')

# Usamos claves distintas ('nombre_entrenador' y 'nombre_pokemon') porque __CRITERION_FUNCTIONS en List es compartido entre todas las instancias, y una clave repetida pisaría el criterio anterior.
 
def by_nombre_entrenador(e):
    return e.nombre
 
def by_nombre_pokemon(p):
    return p.nombre

# cargamos los datos
 
entrenadores = List()
entrenadores.add_criterion('nombre_entrenador', by_nombre_entrenador)
 
ash = Entrenador('Ash', 4, 120, 30)
ash.pokemons.add_criterion('nombre_pokemon', by_nombre_pokemon)
ash.pokemons.append(Pokemon('Pikachu', 45, 'Eléctrico', 'Ninguno'))
ash.pokemons.append(Pokemon('Charizard', 50, 'Fuego', 'Volador'))
ash.pokemons.append(Pokemon('Bulbasaur', 30, 'Planta', 'Veneno'))
ash.pokemons.append(Pokemon('Tyrantrum', 55, 'Roca', 'Dragón'))
 
misty = Entrenador('Misty', 2, 80, 40)
misty.pokemons.add_criterion('nombre_pokemon', by_nombre_pokemon)
misty.pokemons.append(Pokemon('Starmie', 42, 'Agua', 'Psíquico'))
misty.pokemons.append(Pokemon('Wingull', 25, 'Agua', 'Volador'))
misty.pokemons.append(Pokemon('Wingull', 25, 'Agua', 'Volador'))  # repetido a propósito, para el punto i
 
brock = Entrenador('Brock', 5, 100, 10)
brock.pokemons.add_criterion('nombre_pokemon', by_nombre_pokemon)
brock.pokemons.append(Pokemon('Onix', 48, 'Roca', 'Tierra'))
brock.pokemons.append(Pokemon('Terrakion', 60, 'Roca', 'Lucha'))
 
giovanni = Entrenador('Giovanni', 1, 30, 25)
giovanni.pokemons.add_criterion('nombre_pokemon', by_nombre_pokemon)
giovanni.pokemons.append(Pokemon('Persian', 38, 'Normal', 'Ninguno'))
 
cynthia = Entrenador('Cynthia', 6, 150, 5)
cynthia.pokemons.add_criterion('nombre_pokemon', by_nombre_pokemon)
cynthia.pokemons.append(Pokemon('Garchomp', 70, 'Dragón', 'Tierra'))
cynthia.pokemons.append(Pokemon('Roserade', 55, 'Planta', 'Veneno'))
cynthia.pokemons.append(Pokemon('Charizard', 52, 'Fuego', 'Volador'))
 
for entrenador in [ash, misty, brock, giovanni, cynthia]:
    entrenadores.append(entrenador)
 
# a
def cantidad_pokemons(nombre_entrenador):
    indice = entrenadores.search(nombre_entrenador, 'nombre_entrenador')
    if indice is not None:
        return entrenadores[indice].pokemons.size()
    return None

print('Cantidad de Pokemons de un entrenador')
nombre = 'Ash'
cantidad = cantidad_pokemons(nombre)
if cantidad is not None:
    print(f'{nombre} tiene {cantidad} Pokémons')
else:
    print(f'{nombre} no está en la lista')

# b
print()
print('Entrenadores con más de 3 torneos ganados')
for e in entrenadores:
    if e.torneos_ganados > 3:
        print(e.nombre)
 
# c
print()
print('Pokemon de mayor nivel del entrenador con más torneos ganados')
 
mejor_entrenador = None
for e in entrenadores:
    if mejor_entrenador is None or e.torneos_ganados > mejor_entrenador.torneos_ganados:
        mejor_entrenador = e
 
if mejor_entrenador is not None and mejor_entrenador.pokemons.size() > 0:
    mejor_pokemon = None
    for p in mejor_entrenador.pokemons:
        if mejor_pokemon is None or p.nivel > mejor_pokemon.nivel:
            mejor_pokemon = p
    print(f'Entrenador con más torneos: {mejor_entrenador.nombre}')
    print(f'Su Pokemon de mayor nivel es: {mejor_pokemon}')

# d
print()
print('Datos completos de un entrenador y sus Pokemons')
nombre = 'Cynthia'
indice = entrenadores.search(nombre, 'nombre_entrenador')
if indice is not None:
    e = entrenadores[indice]
    print(e)
    for p in e.pokemons:
        print(f'   {p}')
else:
    print(f'{nombre} no está en la lista')

# e
print()
print('Entrenadores con más del 79% de batallas ganadas')
for e in entrenadores:
    total_batallas = e.batallas_ganadas + e.batallas_perdidas
    if total_batallas > 0:
        porcentaje = (e.batallas_ganadas / total_batallas) * 100
        if porcentaje > 79:
            print(f'{e.nombre} - {porcentaje:.1f}%')

# f
print()
print('Entrenadores con (Fuego y Planta) o (Agua/Volador)')
for e in entrenadores:
    tiene_fuego = any(p.tipo == 'Fuego' for p in e.pokemons)
    tiene_planta = any(p.tipo == 'Planta' for p in e.pokemons)
    tiene_agua_volador = any(p.tipo == 'Agua' and p.subtipo == 'Volador' for p in e.pokemons)
 
    if (tiene_fuego and tiene_planta) or tiene_agua_volador:
        print(e.nombre)

# g
print()
print('Promedio de nivel de los Pokemons de un entrenador')
nombre = 'Ash'
indice = entrenadores.search(nombre, 'nombre_entrenador')
if indice is not None:
    e = entrenadores[indice]
    if e.pokemons.size() > 0:
        promedio = sum(p.nivel for p in e.pokemons) / e.pokemons.size()
        print(f'Promedio de nivel de los Pokémons de {e.nombre}: {promedio:.1f}')
    else:
        print(f'{e.nombre} no tiene Pokémons cargados')
else:
    print(f'{nombre} no está en la lista')

# h
print()
print('Cantidad de entrenadores que tienen a un Pokémon')
nombre_pokemon = 'Wingull'
cantidad = 0
for e in entrenadores:
    if any(p.nombre == nombre_pokemon for p in e.pokemons):
        cantidad += 1
print(f'{cantidad} entrenador/es tiene/n a {nombre_pokemon}')

# i
print()
print('Entrenadores con Pokémons repetidos')
for e in entrenadores:
    nombres = [p.nombre for p in e.pokemons]
    if len(nombres) != len(set(nombres)):
        print(e.nombre)

# j
print()
print('Entrenadores con Tyrantrum, Terrakion o Wingull')
buscados = ('Tyrantrum', 'Terrakion', 'Wingull')
for e in entrenadores:
    if any(p.nombre in buscados for p in e.pokemons):
        print(e.nombre)

# k
print()
print('¿El entrenador X tiene al Pokémon Y?')
nombre_entrenador = input('Ingrese el nombre del entrenador: ')
nombre_pokemon = input('Ingrese el nombre del Pokémon: ')
 
indice_entrenador = entrenadores.search(nombre_entrenador, 'nombre_entrenador')
 
if indice_entrenador is not None:
    e = entrenadores[indice_entrenador]
    indice_pokemon = e.pokemons.search(nombre_pokemon, 'nombre_pokemon')
 
    if indice_pokemon is not None:
        p = e.pokemons[indice_pokemon]
        print(f'{e.nombre} sí tiene a {p.nombre}. Datos:')
        print(e)
        print(p)
    else:
        print(f'{e.nombre} no tiene a {nombre_pokemon}')
else:
    print(f'El entrenador {nombre_entrenador} no está en la lista')