# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, sin perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.

from queue_ import Queue 
from stack import Stack 

queue = Queue()

queue.arrive(("10:15", "Facebook", "Juan comentó tu foto"))
queue.arrive(("11:20", "Instagram", "María comenzó a seguirte"))
queue.arrive(("11:50", "Twitter", "Aprendiendo Python con pilas"))
queue.arrive(("12:30", "Facebook", "A Pedro le gusta tu publicación"))
queue.arrive(("14:10", "Twitter", "Python es un gran lenguaje"))
queue.arrive(("16:05", "WhatsApp", "Nuevo mensaje recibido"))

queue.show()

# la función con parámetro funciona mejor porque recibe la cola explícitamente, caso contrario queda "atada" a una queue global
def delete_facebook(queue):

  # para asegurarnos que la auxiliar empiece vacía
  queue_aux = Queue()
  
  while queue.size() > 0:
    value = queue.attention()
    if value[1] != "Facebook":
      queue_aux.arrive(value)
  
  while queue_aux.size() > 0:
    value = queue_aux.attention()
    queue.arrive(value)

delete_facebook(queue)
print()
queue.show()

def show_tweets_python(queue): 

  # para asegurarnos que la auxiliar empiece vacía
  queue_aux = Queue()

  while queue.size() > 0:
    value = queue.attention()
    if value[1] == "Twitter" and "Python" in value[2]:
        print(value)
    queue_aux.arrive(value)

  while queue_aux.size() > 0:
    value = queue_aux.attention()
    queue.arrive(value)

print()
show_tweets_python(queue)

print()
queue.show()

stack = Stack()
queue_aux = Queue()

while queue.size() > 0:
  value = queue.attention()
  if "11:43" <= value[0] <= "15:57":
    stack.push(value)

  queue_aux.arrive(value)

while queue_aux.size() > 0:
  value = queue_aux.attention()
  queue.arrive(value)

print()
stack.show()
print(stack.size())