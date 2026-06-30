'''
COLA (queue):
- Es otra colección de elementos, más común en el ámbito informática que la pila
- El procesador de una máquina se maneja con una queue de procesos
- Los ARRIBOS o INSERCIONES siempre van a ser por el FINAL y las ATENCIONES siempre por el FRENTE
- Cambia el principio de funcionamiento: FIFO (primero que entra es el primero que sale)
- Los elementos estan ordenados por orden de llegada
- Solo se puede acceder al elemento que está en el frente (el cajero el primer elemento que ve es el que está adelante, el resto no sabe)
- La cola tiene un mecanismo que permite gestionar la prioridad de los elementos (después lo vamos a retomar)
- A continuación vamos a modelar la interfaz para resolver los ejercicios
'''
from typing import Any

class Queue:

  def __init__(self):
      self.__elements = []

  # los que llegan van al final
  def arrive(self, value: Any) -> None:
    self.__elements.append(value)
  
  # se atiende por el frente, saco el primer elemento de la cola y se elimina
  def attention(self):
    return self.__elements.pop(0)   

  def size(self) -> int:
    return len(self.__elements)  
  
  # devuelve el elemento que está en el frente sin eliminarlo
  def on_front(self) -> Any:
    if self.size() > 0:
      return self.__elements[0]
  
  # tomo el elemento que está al principio y lo muevo al final
  def move_to_end(self) -> Any: # otra alternativa es que retorne None
     value = self.__elements.pop(0)
     self.__elements.append(value)
     return value

  def show(self) -> None:
     # print(self.__elements) #por ahora lo dejamos así para probar que funcione pero en teoría no lo podemos hacer, la idea es hacer un barrido respetando la naturaleza de la estructura de datos
     queue_aux = Queue()

     for i in range(len(self.__elements)): # uso for porque el while sería infinito porque con move_to_end la cola no se vacía nunca
       #en stack no se podía hacer esto porque la inserción y eliminación se hacen en el mismo lugar, necesitabamos una estructura extra para no perder la información y volver a reconstruir
       value = self.move_to_end()
       print(value)

    #  while self.size() > 0:
    #    #atiendo un elemento de la cola y lo mando a la auxiliar
    #    value = self.attention()
    #    print(value)
    #    queue_aux.arrive(value)
     
    #  while queue_aux.size() > 0:
    #    value = queue_aux.attention()
    #    self.arrive(value)

     # el profe usa en lugar del segundo while: self.__elements = queue_aux.__elements

# q = Queue()

# q.arrive(3)
# q.arrive(7)
# q.show()
# print(q.attention())
# q.arrive(6)
# q.arrive(13)
# q.show()
# print(f'tamaño: {q.size()}')
# print(q.on_front())
# q.move_to_end()
# q.show()