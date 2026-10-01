# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

# Nota: La búsqueda por proximidad/coincidencia se agregó a la clase BinaryTree en tree.py. Los métodos más específicos están en una subclase que hereda de BinaryTree.

from super_heroes_data import superheroes
from tree import BinaryTree

class MarvelCharacter():

    def __init__(self, nombre, anio, casa, bio):
        self.name = nombre
        self.year = anio
        self.house = casa
        self.bio = bio

    def __str__(self):
        return f"{self.name} - {self.year} - {self.house}"
    
class BinaryTreeMarvel(BinaryTree):
    def inorden_villain(self) -> None:
        
      def __inorden_villain(root):
          if root.left is not None:
              __inorden_villain(root.left)

          if root.other_values['is_villain']:
              print(root.value)

          if root.right is not None:
              __inorden_villain(root.right)

      if self.root is not None:
        __inorden_villain(self.root)

    def postorden_hero(self):
        
      def __postorden_hero(root):
          if root.right is not None:
              __postorden_hero(root.right)
          if not root.other_values['is_villain']:
              print(root.value)
          if root.left is not None:
              __postorden_hero(root.left)

      if self.root is not None:
        __postorden_hero(self.root)
    
    def inorden_hero_star_with(self, prefix: str) -> None:
        
        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and not root.other_values['is_villain']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        if self.root is not None:
          __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, text: str) -> None:
        
        def __proxy_search(root, text):
            if root.left is not None:
                __proxy_search(root.left, text)
            if text in root.value.lower():
                print(root.value)
            if root.right is not None:
                __proxy_search(root.right, text)

        if self.root is not None:
          __proxy_search(self.root, text)

    def count_heroes(self) -> int:
      def __count_heroes(root):
          count = 0
          if root is not None:
              if root.left is not None:
                  count += __count_heroes(root.left)
              if not root.other_values['is_villain']:
                  count += 1
              if root.right is not None:
                  count += __count_heroes(root.right)
          return count

      count = __count_heroes(self.root)
      return count

arbol_marvel = BinaryTreeMarvel()

print(f'cantidad de elementos {len(superheroes)}')

# A
for marvel_character in superheroes:
    arbol_marvel.insert_node(marvel_character['name'], other_value=marvel_character)

# # B
# arbol_marvel.inorden_villain()

# # C
# arbol_marvel.inorden_hero_star_with('C')

# #D
# print(f'cantidad de heroes: {arbol_marvel.count_heroes()}')

# E
search_str = input('ingrese lo que quiere buscar: ')
arbol_marvel.proxy_search(search_str.lower())

search_str = input('ingrese lo que quiere modificar: ')

node = arbol_marvel.search(search_str)
if node is not None:
    new_name = input('ingrese el nuevo nombre: ')
    delete_value, delete_other_value = arbol_marvel.delete_node(node.value)
    delete_other_value['name'] = new_name
    arbol_marvel.insert_node(new_name, delete_other_value)

print()
arbol_marvel.inorden_hero_star_with('D')

# F
# arbol_marvel.postorden_hero()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
arbol_heroes = BinaryTreeMarvel()
arbol_villanos = BinaryTreeMarvel()

# función recursiva: recibe un nodo del árbol original, va a visitar ese nodo y luego todos sus descendentes
def separar_heroes_y_villanos(nodo):
    # caso base: si el nodo no existe, la función termina
    if nodo is None:
        return
 
    # Evaluar el nodo actual
    # si nodo.other_values es verdadero (tiene contenido)
    if nodo.other_values:
      # .get() es un método de los diccionarios que busca una clave 
      # si la clave 'is_villain' existe, devuelve su valor (True o False), si no existe, devuelve el segundo argumento (False) por default
      is_villain = nodo.other_values.get('is_villain', False)
    # si other_values es None o está vacío, ni siquiera se intenta llamar a .get() (porque None.get(...) daría un error). Directamente se asigna False. 
    else:
      is_villain = False

    # operador ternario de Python: valor_si_verdadero if condicion else valor_si_falso
    # is_villain = nodo.other_values.get('is_villain', False) if nodo.other_values else False

    # insertar en el árbol correspondiente
    if is_villain:
        arbol_villanos.insert_node(nodo.value, nodo.other_values)
    else:
        arbol_heroes.insert_node(nodo.value, nodo.other_values)
 
    # Recorrer subárboles (recursión)
    # este recorrido es de tipo preorden (primero nodo actual, luego izquierda, luego derecha)
    separar_heroes_y_villanos(nodo.left)
    separar_heroes_y_villanos(nodo.right)
 
# iniciar el proceso (se llama a la función con la raíz original y arranca todo)
separar_heroes_y_villanos(arbol_marvel.root)
 
# I. Determinar cuántos nodos tiene cada árbol
cantidad_heroes = arbol_heroes.count_nodes()
cantidad_villanos = arbol_villanos.count_nodes()

print(f"Cantidad de superhéroes: {cantidad_heroes}")
print(f"Cantidad de villanos: {cantidad_villanos}")
 
# II. Barrido ordenado alfabéticamente de cada árbol (Inorden)
print("Superhéroes ordenados alfabéticamente")
arbol_heroes.inorden()
 
print("Villanos ordenados alfabéticamente")
arbol_villanos.inorden()