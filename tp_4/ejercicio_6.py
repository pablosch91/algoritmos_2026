# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar las funciones necesarias para poder realizar las siguientes actividades:
# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from list_ import List

# defino la lista
list_heroes = List()

# defino la clase
class SuperHeroe:

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    # sobreescribimos el método que se llama cuando hacemos el print de un objeto, sin este método, el print no sabe cómo mostrarlo y muestra la posición de memoria
    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}" # podría ser solamente el nombre

# cargo los datos
list_heroes.append(SuperHeroe("Linterna Verde", 1940, "DC", "Miembro de los Green Lantern Corps."))
list_heroes.append(SuperHeroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium."))
list_heroes.append(SuperHeroe("Dr. Strange", 1963, "DC", "Hechicero supremo que utiliza magia."))
list_heroes.append(SuperHeroe("Iron Man", 1963, "Marvel", "Usa una armadura tecnológica."))
list_heroes.append(SuperHeroe("Batman", 1939, "DC", "Justiciero que utiliza traje y gadgets."))
list_heroes.append(SuperHeroe("Superman", 1938, "DC", "Último hijo de Krypton."))
list_heroes.append(SuperHeroe("Mujer Maravilla", 1941, "DC", "Princesa amazona y guerrera."))
list_heroes.append(SuperHeroe("Capitana Marvel", 1968, "Marvel", "Heroína con poderes cósmicos."))
list_heroes.append(SuperHeroe("Flash", 1940, "DC", "El hombre más rápido del mundo."))
list_heroes.append(SuperHeroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia."))
list_heroes.append(SuperHeroe("Black Widow", 1964, "Marvel", "Espía experta en combate."))
list_heroes.append(SuperHeroe("Spider-Man", 1962, "Marvel", "Héroe que utiliza un traje especial."))

# defino los criterios que necesito (para saber cuál usar tenemos que ver qué se nos pide, por nombre seguro)
def by_name(item):
    return item.name

def by_year(item):
    return item.year

# agregamos ese criterio a la lista
list_heroes.add_criterion('name', by_name)
list_heroes.add_criterion('year', by_year)

# empezamos a trabajar

# a. eliminar el nodo que contiene la información de Linterna Verde;

deleted_value = list_heroes.delete_value('Linterna Verde', 'name')
print(f'Valor eliminado: {deleted_value}')

print()
print('Hacemos un barrido para chequear:')
list_heroes.show()

# b. mostrar el año de aparición de Wolverine;
print()
wolverine = list_heroes.search('Wolverine', 'name')
if wolverine is not None:
  print(f'Año de aparicion de {list_heroes[wolverine].name} es {list_heroes[wolverine].year}')
else:
    print('No está en la lista')

# c. cambiar la casa de Dr. Strange a Marvel;
dr_strange = list_heroes.search('Dr. Strange', 'name')
if dr_strange is not None:
  list_heroes[dr_strange].house = 'Marvel'

print()
print('Cambiamos la casa de Dr Strange a Marvel:')
list_heroes.show()

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
print()
print('Superhéroes que en su biografía menciona la palabra “traje” o “armadura”:')
for heroe in list_heroes:
    if any(palabra in heroe.bio.lower() for palabra in ["traje", "armadura"]):
        print(heroe.name)

# any() deja de buscar cuando encuentra el primer True

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
print()
print('Nombre y casa de los superhéroes con fecha de aparición anterior a 1963:')
for hero in list_heroes:
    if hero.year < 1963:
        print(f'{hero.name} - {hero.house}')

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# busco por nombre, si lo encuentro, muestro la casa y ya está
print()

for name in ['Capitana Marvel', 'Mujer Maravilla']:
    index = list_heroes.search(name, 'name')
    if index is not None:
        hero = list_heroes[index]
        print(f'La casa de {hero.name} es {hero.house}')

# g. mostrar toda la información de Flash y Star-Lord;
print()
for name in ['Flash', 'Star-Lord']:
    index = list_heroes.search(name, 'name')
    if index is not None:
        hero = list_heroes[index]
        print(f'La información de {hero.name} es {hero.name} - {hero.year} - {hero.house} - {hero.bio}')

# h. listar los superhéroes que comienzan con la letra B, M y S;
print()
print('Superhéroes que comienzan con la letra B, M o S:')
for heroe in list_heroes:
    if heroe.name.startswith(("B", "M", "S")):
        print(heroe.name)

# "Batman".startswith("B") da True

# i. determinar cuántos superhéroes hay de cada casa de comic.
print()

print(f'Cantidad de superhéroes en la lista: {len(list_heroes)}')

marvel = 0
dc = 0

for hero in list_heroes:
    if hero.house == 'Marvel':
        marvel += 1
    elif hero.house == 'DC':
        dc += 1

print(f'Superhéroes de Marvel: {marvel}')
print(f'Superhéroes de DC: {dc}')
    

# puede pasar que me pidan un listado ordenado por año de aparición
print()
print('Listado ordenado por año de aparición:')
list_heroes.sort_by_criterion('year')
list_heroes.show()