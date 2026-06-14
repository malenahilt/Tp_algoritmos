from cola import Queue
from pila import Stack

cola = Queue()
cola.arrive({'nombre': 'Tony Stark', 
             'superheroe': 'Iron-man',
             'genero': 'M'})
cola.arrive({'nombre': 'Steve Rogers',
             'superheroe': 'Capitan America',
             'genero': 'M'})
cola.arrive({'nombre': 'Natasha Romanoff',
             'superheroe': 'Black Widow',
             'genero': 'F'})
cola.arrive({'nombre': 'Carol Danvers',
             'superheroe': 'Capitana Marvel',
             'genero': 'F'})
cola.arrive({'nombre': 'Scott Lang',
             'superheroe': 'Ant-Man',
             'genero': 'M'})

print()
cola.show()
#a)determinar el nombre del personaje de la superhéroe Capitana Marvel;
tamaño_cola = cola.size()
for i in range (tamaño_cola):
   heroe = cola.on_front()
   if heroe['superheroe'] == 'Capitana Marvel':
      print(f'el nombre de la superheroina {heroe["superheroe"]} es {heroe["nombre"]}')
      cola.move_to_end()
   else:
      cola.move_to_end()
   
#b)mostrar los nombre de los superhéroes femeninos;
print('las super heroinas mujeres son: ')
for i in range(tamaño_cola):
   femenino = cola.on_front()
   if femenino['genero'] == 'F':
      print(f'-{femenino["superheroe"]}')
      cola.move_to_end()
   else:
      cola.move_to_end()

#c)mostrar los nombres de los personajes masculinos;
print('el nombre de los heroes masculinos son: ')
for i in range (tamaño_cola):
   masculino = cola.on_front()
   if masculino['genero'] == 'M':
      print(f'-{masculino["nombre"]}')
      cola.move_to_end()
   else:
      cola.move_to_end()

#d)determinar el nombre del superhéroe del personaje Scott Lang;

for i in range(tamaño_cola):
   buscado = cola.on_front()
   if buscado['nombre'] == 'Scott Lang':
      print(f'el nombre de superheroe de {buscado["nombre"]} es: {buscado["superheroe"]}')
      cola.move_to_end()
   else:
      cola.move_to_end()

#e)mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
print('personajes que inician con la letra S: ')
for i in range (tamaño_cola):
   inicial = cola.on_front()
   if inicial['nombre'].startswith('S'):
      print(f'-{inicial["nombre"]}, {inicial["superheroe"]}, {inicial["genero"]}')
      cola.move_to_end()
   else:
      cola.move_to_end()

#f)determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.

for i in range (tamaño_cola):
   buscado = cola.on_front()
   if buscado['nombre'] == 'Carol Danvers':
      print(f'el nombre de superheroe de {buscado["nombre"]} es: {buscado["superheroe"]}')
      cola.move_to_end()
   else: 
      cola.move_to_end()

