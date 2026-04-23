'''
Con cada estructura de datos vamos a ver cómo operan, cómo se administran y para qué casos particulares nos sirven.
PILA: es una sucesión de elementos que están uno encima del otro (vamos a implementarla de forma dinámica). Ejemplos:
En la vida cotidiana: apilar libros, ropa, cajas, etc.
En informática: deshacer y rehacer acciones, navegar hacia atrás y adelante en un navegador, etc.
Funcionamiento:
- Tiene dos acciones principales: apilar (equivalente a insertar) y desapilar (equivalente a eliminar). Sin ellas no hay pila.
- Sólo se puede acceder al último elemento que está en la cima (el único que podemos conocer), por esta razón no se puede hacer una búsqueda (tengo que desapilar).
- Se rige bajo el principio LIFO (Last In, First Out): el último que entra es el primero que sale.
- Los datos no van a seguir un orden tradicional (ascendente, descendente, por nombre, por apellido, por código) sino que van a estar ordenados por el orden cronológico que fueron apilados.
'''

from typing import Any
from copy import copy, deepcopy

class Stack:

  # elements = []

  def __init__(self):
    self.__elements = []

  # apilar, no devuelve nada
  def push(self, value: Any) -> None:
    self.__elements.append(value) # siempre agregamos un elemento al final, por eso usamos append y no insert
  
  # desapilar, como en la pila puede haber cualquier elemento, devuelve Any
  def pop(self) -> Any:
    return self.__elements.pop()
  
  # mostrar
  def show(self):
    #print(self.__elements) no es del todo correcto porque en teoría no tengo acceso a todos los elementos, solo al de la cima
    stack_aux = Stack()

    # # forma tradicional
    # while self.size() > 0:
    #   #barro sobre la pila, muestro los elementos y los guardo sobre la pila auxiliar
    #   # Usar 'value' evita llamar a pop() dos veces (pop() modifica la pila)
    #   value = self.pop()
    #   print(value)
    #   stack_aux.push(value)
    
    # while stack_aux.size() > 0:
    #   #barro sobre la estructura auxiliar y los pongo sobre la pila original sin mostrar
    #   value = stack_aux.pop()
    #   self.push(value)
    
    # print(self.__elements)

    # forma alternativa (no es válida en todos los lenguajes)
    # importar copy

    stack_aux.__elements = copy(self.__elements)

    while stack_aux.size() > 0: # el bucle termina cuando pila.size() == 0
        value = stack_aux.pop()
        print(value)

  # devuelve la cantidad de elementos (entero)
  def size(self) -> int:
    return len(self.__elements)

  # retorna el último elemento (lo que está en la cima) sin quitarlo
  # tiene un chequeo para que no nos falle si el usuario llama a un top y no hay elementos en la pila
  def on_top(self) -> Any:
    if self.size() > 0: #si no se cumple esto, no retorna nada
      return self.__elements[-1]
  
# pila = Stack()

# pila.push(1)
# print(pila) # nos devuelve una posición de memoria
# # print(pila.elements) # [1]
# # pila.show()

# pila.push(2)
# # print(pila.elements) # [1, 2]
# pila.show()
# print(f'elemento en la cima {pila.on_top()}')

# # pila.elements.clear() # elimina todos los elementos
# # cuando el ususario quiere hacer un comportamiento fuera de lo normal, como el atributo es privado, no va a poder (por más que le pongamos adelante __)

# aux = pila.pop() #auxiliar para guardar lo que saco
# print(f'elemento eliminado {aux}')

# pila.push(3)
# # print(pila.elements) # [3]

# pila.push(4)
# # print(pila.elements) # [3, 4]
# pila.show()

# # no estamos respetando la naturaleza o principio de la pila, tenemos que garantizar que se cumpla el principio de funcionamiento: si quiero quitar elementos, tengo que empezar por el último, no puedo administrarlos como quiera

# # logramos restringir y asegurar que la estructura se va a comportar como queremos sino el comportamiento iba a quedar sujeto a lo que haga el desarrollador y no es la idea

# # necesitamos listar para chequear aunque no sea una actividad natural