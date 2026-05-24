from typing import Any
from copy import copy, deepcopy

class Stack:

  # elements = []

  def __init__(self):
    self.__elements = []

  # apilar, no devuelve nada
  def push(self, value: Any) -> None:
    self.__elements.append(value) # siempre apilamos elementos uno encima de otro, por eso usamos append (agrega al final) y no insert
  
  # desapilar, como en la pila puede haber cualquier elemento, devuelve Any
  def pop(self) -> Any:
    return self.__elements.pop()
  
  # mostrar, necesitamos listar para chequear aunque no sea una actividad natural
  def show(self) -> Any:
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
    
    # forma alternativa (no es válida en todos los lenguajes), importar copy

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