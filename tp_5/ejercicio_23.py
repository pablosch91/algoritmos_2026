# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla (ver en página 169 del libro) y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

# Nota: La búsqueda por proximidad/coincidencia se agregó a la clase BinaryTree en tree.py. Los métodos más específicos están en una subclase que hereda de BinaryTree.

from tree import BinaryTree

nombres = [
    'Ceto', 'Tifón', 'Equidna', 'Dino', 'Pefredo', 'Enio',
    'Escila', 'Caribdis', 'Euríale', 'Esteno', 'Medusa',
    'Ladón', 'Águila del Cáucaso', 'Quimera',
    'Hidra de Lerna', 'León de Nemea', 'Esfinge',
    'Dragón de la Cólquida', 'Cerbero', 'Cerda de Cromión',
    'Ortro', 'Toro de Creta', 'Jabalí de Calidón',
    'Carcinos', 'Gerión', 'Cloto', 'Láquesis', 'Átropos',
    'Minotauro de Creta', 'Harpías', 'Argos Panoptes',
    'Aves del Estínfalo', 'Talos', 'Sirenas', 'Pitón',
    'Cierva de Cerinea', 'Basilisco', 'Jabalí de Erimanto'
]

derrotados_por = [
    None, 'Zeus', 'Argos Panoptes', None, None, None,
    None, None, None, None, 'Perseo',
    'Heracles', None, 'Belerofonte',
    'Heracles', 'Heracles', 'Edipo',
    None, None, 'Teseo',
    'Heracles', 'Teseo', 'Atalanta',
    None, 'Heracles', None, None, None,
    'Teseo', None, 'Hermes',
    None, 'Medea', None, 'Apolo',
    None, None, None
]


class Criatura:

    def __init__(self, derrotado_por):
        self.derrotado_por = derrotado_por
        self.descripcion = ''
        self.capturada = None


def texto(valor):
    if valor is None or valor == '':
        return '-'
    return valor


def mostrar_criatura(nodo):
    print(f'Criatura: {nodo.value}')
    print(f'  Derrotada por: {texto(nodo.other_values.derrotado_por)}')
    print(f'  Capturada por: {texto(nodo.other_values.capturada)}')
    print(f'  Descripción: {texto(nodo.other_values.descripcion)}')

class BinaryTreeCriaturas(BinaryTree):

    # a
    def inorden_criaturas(self) -> None:
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(
                    f'{root.value} - derrotada por: '
                    f'{texto(root.other_values.derrotado_por)}'
                )
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    # b
    def cargar_descripcion(self, nombre: str, descripcion: str) -> None:
        nodo = self.search(nombre)
        if nodo is None:
            print(f'No existe la criatura {nombre}')
        else:
            nodo.other_values.descripcion = descripcion

    # c
    def mostrar_info(self, nombre: str) -> None:
        nodo = self.search(nombre)
        if nodo is None:
            print(f'No existe la criatura {nombre}')
        else:
            mostrar_criatura(nodo)

    # d
    def top_heroes(self) -> None:
        heroes = []
        cantidades = []

        def __contar_heroes(root):
            if root is not None:
                __contar_heroes(root.left)
                heroe = root.other_values.derrotado_por
                if heroe is not None:
                    if heroe in heroes:
                        pos = heroes.index(heroe)
                        cantidades[pos] += 1
                    else:
                        heroes.append(heroe)
                        cantidades.append(1)
                __contar_heroes(root.right)

        __contar_heroes(self.root)

        if not heroes:
            print('No hay héroes o dioses registrados.')
            return

        print('Los héroes o dioses que derrotaron más criaturas:')
        cantidad_puestos = min(3, len(heroes))
        cantidad_tercero = 0

        for i in range(cantidad_puestos):
            mayor = 0
            for j in range(len(heroes)):
                if cantidades[j] > cantidades[mayor]:
                    mayor = j

            print(f'  {i + 1}. {heroes[mayor]}: {cantidades[mayor]}')

            if i == 2:
                cantidad_tercero = cantidades[mayor]

            cantidades[mayor] = -1

        if cantidad_puestos == 3:
            print(
                f'Otros con {cantidad_tercero} '
                f'derrotada(s), empatados en el 3° puesto:'
            )
            for j in range(len(heroes)):
                if cantidades[j] == cantidad_tercero:
                    print(f'  {heroes[j]}')

    # e
    def derrotadas_por(self, heroe: str) -> None:
        def __derrotadas_por(root):
            if root is not None:
                __derrotadas_por(root.left)
                if root.other_values.derrotado_por == heroe:
                    print(f'  {root.value}')
                __derrotadas_por(root.right)

        __derrotadas_por(self.root)

    # f
    def no_derrotadas(self) -> None:
        def __no_derrotadas(root):
            if root is not None:
                __no_derrotadas(root.left)
                if root.other_values.derrotado_por is None:
                    print(f'  {root.value}')
                __no_derrotadas(root.right)

        __no_derrotadas(self.root)

    # g / h
    def capturar(self, nombre: str, heroe: str) -> None:
        nodo = self.search(nombre)
        if nodo is None:
            print(f'No existe la criatura {nombre}')
        else:
            nodo.other_values.capturada = heroe

    # i, j, k y m en tree.py

    # l
    def renombrar(self, viejo: str, nuevo: str) -> None:
        x, datos = self.delete_node(viejo)
        if x is None:
            print(f'No existe la criatura {viejo}')
        else:
            self.insert_node(nuevo, datos)

    # n
    def capturadas_por(self, heroe: str) -> None:
        def __capturadas_por(root):
            if root is not None:
                __capturadas_por(root.left)
                if root.other_values.capturada == heroe:
                    print(f'  {root.value}')
                __capturadas_por(root.right)

        __capturadas_por(self.root)

arbol = BinaryTreeCriaturas()

for i in range(len(nombres)):
    arbol.insert_node(nombres[i], Criatura(derrotados_por[i]))

print(f'Nodos cargados: {arbol.count_nodes()}')

# El orden en el programa principal responde a la secuencia lógica de las dependencias de los datos que exige la consigna

# a
print()
print('Listado inorden')
arbol.inorden_criaturas()

# b
print()
print('Cargar descripciones')
arbol.cargar_descripcion(
    'Talos', 'Gigante de bronce que protegía la isla de Creta.'
)
arbol.cargar_descripcion(
    'Cerbero', 'Perro de tres cabezas que custodia el Hades.'
)
arbol.cargar_descripcion(
    'Ladón', 'Dragón que custodiaba las manzanas de oro de las Hespérides.'
)

# c
print()
print('Información de Talos')
arbol.mostrar_info('Talos')

# g / h
print()
print('Heracles capturó a las siguientes criaturas')
atrapadas = [
    'Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto'
]
for criatura in atrapadas:
    arbol.capturar(criatura, 'Heracles')

# i
print()
print('Búsqueda por coincidencia')
textos = ['ja', 'er', 'xyz']
for texto_buscado in textos:
    print(f"Coincidencias con '{texto_buscado}':")
    arbol.proxy_search(texto_buscado)

# j
print()
print('Eliminar Basilisco y Sirenas')
x, _ = arbol.delete_node('Basilisco')
print(f'Eliminada: {x}')
x, _ = arbol.delete_node('Sirenas')
print(f'Eliminada: {x}')

# k
print()
print('Modificar las Aves del Estínfalo')
aves = arbol.search('Aves del Estínfalo')
if aves is not None:
    aves.other_values.derrotado_por = 'Heracles'
    aves.other_values.descripcion = 'Heracles derrotó a varias.'
    mostrar_criatura(aves)
else:
    print('No se encontraron las Aves del Estínfalo')

# d
print()
print('Top 3 héroes')
arbol.top_heroes()

# e
print()
print('Criaturas derrotadas por Heracles')
arbol.derrotadas_por('Heracles')

# f
print()
print('Criaturas no derrotadas')
arbol.no_derrotadas()

# l
print()
print('Ladón -> Dragón Ladón')
arbol.renombrar('Ladón', 'Dragón Ladón')
arbol.mostrar_info('Dragón Ladón')

# m
print()
print('Listado por nivel')
arbol.by_level()

# n
print()
print('Criaturas capturadas por Heracles')
arbol.capturadas_por('Heracles')