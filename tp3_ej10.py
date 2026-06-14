from cola import Queue
from pila import Stack

cola = Queue()
cola.arrive({'app' :'Instagram ',
'hora': '12:00 ',
'mensaje':'Compartio una publicacion '})
cola.arrive({'app': 'Whatsapp ',
'hora': '11:43 ',
'mensaje': 'mama: A que hora llegas? '})
cola.arrive({'app': 'Facebook ',
'hora': '00:00 ',
'mensaje': '@x le dio me gusta a la publicacion'})
cola.arrive({'app': 'Twitter ',
'hora': '00:30 ',
'mensaje': 'nuevo curso de python gratuito'})

print('-----cola original-----')
cola.show()
#a)
cola_Tamaño = cola.size()

def eliminar_app(cola)-> any:
    for i in range(cola_Tamaño):
        if cola.on_front()['app'] == 'Facebook ':
         cola.attention()
        else:
            cola.move_to_end()

eliminar_app(cola)

print()
print('-----eliminar app-----')
cola.show()
#b)escribir una función que muestre las notificaciones de Twitter, cuyo mensaje incluya
#la palabra ‘Python’, si perder datos en la cola;

def not_Twitter(cola)->any:
   for i in range (cola_Tamaño):
      notificacion = cola.on_front()
      if notificacion['app'] == 'Twitter ' and 'python' in notificacion['mensaje']:
        print(f"Twitter: [{notificacion['hora']}]{notificacion['mensaje']}")
        cola.move_to_end()
      else:
         cola.move_to_end()

print()
print('-----notificacion app-----')
not_Twitter(cola)
#c) utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
#11:43 y las 15:57, y determinar cuántas son.
pila = Stack()
cont = 0
for i in range(cola_Tamaño-1):
   notificacion = cola.on_front()
   if notificacion['hora'] >= '11:43' and notificacion['hora'] <= '15:57':
      pila.push(notificacion)
      cont += 1   
      cola.move_to_end()
   else:
      cola.move_to_end()

print()
print('-----pila temporal-----')
pila.show()
print()
print(f'la cantidad de notificaciones comprendidas entre la hora 11:43 y 15:57 son {cont}')