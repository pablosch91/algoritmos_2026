# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc.-, desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from queue_ import Queue

queue = Queue()

queue.arrive(("Tony Stark", "Iron Man", "M"))
queue.arrive(("Steve Rogers", "Capitán América", "M"))
queue.arrive(("Natasha Romanoff", "Black Widow", "F"))
queue.arrive(("Thor Odinson", "Thor", "M"))
queue.arrive(("Bruce Banner", "Hulk", "M"))
queue.arrive(("Clint Barton", "Hawkeye", "M"))
queue.arrive(("Peter Parker", "Spider-Man", "M"))
queue.arrive(("Stephen Strange", "Doctor Strange", "M"))
queue.arrive(("Wanda Maximoff", "Scarlet Witch", "F"))
queue.arrive(("Carol Danvers", "Capitana Marvel", "F"))
queue.arrive(("Scott Lang", "Ant-Man", "M"))
queue.arrive(("Hope Van Dyne", "Wasp", "F"))
queue.arrive(("TChalla", "Black Panther", "M"))
queue.arrive(("Sam Wilson", "Falcon", "M"))
queue.arrive(("Bucky Barnes", "Winter Soldier", "M"))
queue.arrive(("Vision", "Vision", "M"))
queue.arrive(("Gamora", "Gamora", "F"))
queue.arrive(("Peter Quill", "Star-Lord", "M"))
queue.arrive(("Rocket Raccoon", "Rocket", "M"))
queue.arrive(("Groot", "Groot", "M"))
queue.arrive(("Nebula", "Nebula", "F"))
queue.arrive(("Shuri", "Shuri", "F"))
queue.arrive(("Loki Laufeyson", "Loki", "M"))
queue.arrive(("Jennifer Walters", "She-Hulk", "F"))
queue.arrive(("Marc Spector", "Moon Knight", "M"))

queue_aux = Queue()

while queue.size() > 0:
  value = queue.attention()

  if value[1] == 'Capitana Marvel':
    print(f'El personaje de Capitana Marvel es: {value[0]}')

  if value[2] == 'F':
    print(f'Superhéroe femenino: {value[1]}')

  if value[2] == 'M':
    print(f'Personaje masculino: {value[0]}')
  
  if value[0] == 'Scott Lang':
    print(f'El superhéroe de Scott Lang es: {value[1]}')

  if value[0].startswith('S') or value[1].startswith('S'):
    print(f'Personaje o superhéroe que comienza con S: {value}')

  if value[0] == 'Carol Danvers':
    print(f'Carol Danvers se encuentra en la cola y su superhéroe es: {value[1]}')
  
  queue_aux.arrive(value)

while queue_aux.size() > 0:
  value = queue_aux.attention()
  queue.arrive(value)