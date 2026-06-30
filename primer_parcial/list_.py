'''
LISTA (list):
- Tiene random access (acceso aleatorio), quiere decir que puedo acceder a cualquier posición sin ninguna restricción
- Ahora la búsqueda es parte de las operaciones básicas: puedo insertar, eliminar o buscar sin ningún tipo de problemas
- Por lo general, nos interesa tener los elementos ordenados, nos facilita hacer una búsqueda eficiente como la búsqueda binaria
- El dato pasa a ser un elemento más importante, en las estructuras anteriores no interesaba el elemento que entre, ya tenía su lugar predestinado
- Ejemplo: lista de archivos, tiene criterios preestablecidos para cambiar su orden (por nombre, fecha, etc)
- Puedo hacer barridos de forma natural (sin hacer cosas extrañas)
- Vamos a hacer una lista tomando parte de la lista nativa de Python con una herencia, sobreescribiendo las acciones que nos interesen
'''
from typing import Any, Optional
 
# definimos clase List que hereda de la clase list de Python (por ejemplo el append), agregándole funcionalidades propias
class List(list):
  # es un diccionario que va a contener las funciones de criterio que le interesa tener al usuario
  __CRITERION_FUNCTIONS = {}
 
  # método que sirve para agregar una función al diccionario
  def add_criterion(self, criterion_key: str, criterion_function) -> None:
    # 'guardar criterion_function en el diccionario __CRITERION_FUNCTIONS usando criterion_key como clave'
    self.__CRITERION_FUNCTIONS[criterion_key] = criterion_function
  
  def show(self) -> None:
    for element in self:
      print(element)
 
  # Si me dicen por qué atributo ordenar, lo uso. Si no me dicen nada y los elementos son simples (int, str, etc.), uso el ordenamiento normal de Python.
  # recibe un criterio de búsqueda
  # no devuelve nada, su trabajo es modificar la lista original
  def sort_by_criterion(self, criterion_key: str = None) -> None:

    # obtener la función de criterio (by_name, by_last_name, by_age, etc.)
    criterion_function = self.__CRITERION_FUNCTIONS.get(criterion_key)

    # si la lista está vacía, salí del método
    if not self:
        return

    # si hay una función de criterio, se ordena por ese criterio
    if criterion_function is not None:
      self.sort(key=criterion_function)
    # si la lista no está vacía (una lista vacía es falsa) y el primer elemento es primitivo (asumimos que todos los demás también lo son), se ordena usando el ordenamiento nativo
    elif self and isinstance(self[0], (bool, int, float, str)):
      self.sort()
    # sino
    else:
      print('No se puede ordenar la lista con el criterio indicado')

  # recibe lo que se quiere buscar y un criterio de búsqueda
  # devuelve la posición donde encontró el elemento o None
  # está adaptado para que funcione cuando el tipo de dato es primitivo y cuando no
  def search(self, search_value: Any, criterion_key: str = None) -> Optional[int]:
 
    # la búsqueda binaria requiere que la lista esté ordenada, por eso antes de buscar la ordena según el criterio indicado
    self.sort_by_criterion(criterion_key=criterion_key)
 
    criterion_function = self.__CRITERION_FUNCTIONS.get(criterion_key)
    
    # inicializamos los límites
    start = 0
    end = len(self) - 1
    middle = (start + end) // 2
 
    while start <= end:
 
      # si los elementos son complejos y no tengo una función de criterio, entonces no puedo realizar la búsqueda
      # print(isinstance(5, int)) # para saber si 5 es una instancia de entero (True)
      if not isinstance(self[0], (bool, int, float, str)) and criterion_function is None:
        print('No se pudo determinar criterio de búsqueda')
        return None
      
      # value = criterion_function(self[middle]) if criterion_function else self[middle]
 
      # si tengo una función de criterio, la uso para obtener el valor del elemento del medio
      if criterion_function:
          value = criterion_function(self[middle])  # extraigo el atributo del objeto en la posición middle
 
      # si no, uso directamente el elemento del medio
      else:
          value = self[middle]  # uso el valor tal cual está en la lista
      
      if search_value == value:
        return middle
      elif search_value < value:
        end = middle - 1
      else: 
        start = middle + 1
      
      middle = (start + end) // 2
 
  # para insertar vamos a mantener el método append (al final) o insert (en cualquier posición)
 
  # recibe lo que se quiere eliminar y un criterio de búsqueda
  # devuelve el elemento eliminado o None si no lo encontró
  def delete_value(self, value, criterion_key: str = None) -> Optional[Any]:
 
    # buscamos la posición de lo que se quiere eliminar
    index = self.search(value, criterion_key)  # si está en la lista devuelve la posición, sino devuelve None (el search ya sabe como manejar un dato primitivo o compuesto)
 
    # return self.pop(index) if index is not None else None
    if index is not None:
       return self.pop(index)
    else:
       return None
 
  def size(self) -> int:
    return len(self)
 
# l.sort() ordena los elementos de menor a mayor y l.sort(reverse = True) ordena de mayor a menor