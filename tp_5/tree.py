from typing import Any, Optional

from queue_ import Queue
class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            # print(root.value)
            aux = None
            if root.right is None:
                # print('mayor encontrado')
                return root.left, root
            else:
                # print('segui buscando a la derecha')
                root.right, aux = __replace(root.right)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    # print('ir a la izq')
                    # input()
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    # print('ir a la derecha')
                    # input()
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    # print('valor encontrado')
                    # input()
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        # print('no tiene hijo izquierdo')
                        # input()
                        return root.right, x, other_value
                    elif root.right is None:
                        # print('no tiene hijo derecho')
                        # input()
                        return root.left, x, other_value
                    else:
                        # print('buscar remplazo')
                        # input()
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values
                        
                root = self.auto_balance(root) 
                self.update_height(root)

            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux
        
        node = __search(self.root, value)
        
        return node 

    def proxy_search(self, text: str) -> None:
        def __proxy_search(root, text):
            if root is not None:
                __proxy_search(root.left, text)
                if text.lower() in root.value.lower():
                    print(root.value)
                __proxy_search(root.right, text)

        if self.root is not None:
            __proxy_search(self.root, text)
    
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    # forma ascendente
    def inorden(self) -> None:
        
        def __inorden(root):
            if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                __inorden(root.left)
            # print(f'procesa nodo actual')
            print(root.value)
            if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                __inorden(root.right)

        __inorden(self.root)
    
    # decisión de diseño: forma descendente (el espejo del inorden)
    def postorden(self) -> None:
        
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    # primero raíz
    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()
    
    # método para "ver" el árbol
    def show(self) -> None:

      def __show(root, level=0, branch='raiz'):
          if root is not None:
              print('   ' * level + f'{branch}: {root.value}')
              __show(root.left, level + 1, 'izq')
              __show(root.right, level + 1, 'der')

      __show(self.root)

    # método para contar nodos
    def count_nodes(self) -> int:
          def __count(root):
              if root is None:
                  return 0
              return 1 + __count(root.left) + __count(root.right)
    
          return __count(self.root)

# class Persona:

#     def __init__(self, nom, ape, dni):
#         self.nom = nom
#         self.ape = ape
#         self.dni = dni

#     def __str__(self):
#         return f"{self.ape} {self.nom} {self.dni}"

# arbol = BinaryTree()
# arbol_ape = BinaryTree()

# p1 = Persona('Pepito', 'Gonzalez', 23)
# p2 = Persona('Pepito', 'Perez', 24)
# p3 = Persona('Pepito', 'Garcia', 25)
# p4 = Persona('Pepito', 'Casanova', 26)

# arbol.insert_node(p1.dni, p1)
# arbol.insert_node(p2.dni, p2)
# arbol.insert_node(p3.dni, p3)
# arbol.insert_node(p4.dni, p4)

# arbol_ape.insert_node(p1.ape, p1)
# arbol_ape.insert_node(p2.ape, p2)
# arbol_ape.insert_node(p3.ape, p3)
# arbol_ape.insert_node(p4.ape, p4)
# arbol.insert_node('B')
# arbol.insert_node('W')
# arbol.insert_node('V')
# arbol.insert_node('F')
# arbol.insert_node('P')
# arbol.insert_node('R')
# for i in range (1, 13):
#     arbol.insert_node(i)

# arbol.inorden()
# print()
# arbol.root = arbol.auto_balance(arbol.root)


# arbol.by_level()

# print(arbol.root.right.left.value)

# arbol.preorden()



            #                                     8
            #                 4                                               10
            #     2                       6                       9                      11
            # 1       3               5       7                                               12
# print()
# print('eliminar', arbol.delete_node('F'))
# print()
# arbol.inorden()

# aux = arbol.search(26)
# if aux is not None:
#     print(f'valor encontrado {aux.other_values}')
# else:
#     print('no encontrado')

# aux = arbol_ape.search('Gonzalez')
# if aux is not None:
#     print(f'valor encontrado {aux.other_values}')
# else:
#     print('no encontrado')
