from lista_heroes import superheroes
from cola import Queue
from lista__ import List

class Heroes:
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name == name
        self.alias == alias
        self.real_name == real_name
        self.short_bio == short_bio
        self.first_appearane == first_appearance
        self.is_villian == is_villain


def __str__(self):
        return(f'{self.name}-{self.alias}-{self.real_name}-{self.short_bio}-{self.first_appearance}-{self.is_villain}')

def by_name(item):
        return item['name']

def by_real_name(item):
        return item['real_name'] or ''

def by_first_appaerance(item):
        return item['first_appearance']

superheroes = List(superheroes)
superheroes.add_criterion('name', by_name)
superheroes.add_criterion('real_name' or '', by_real_name)
superheroes.add_criterion('first_appearance', by_first_appaerance)
superheroes.show()
print()

##A) Listado ordenado de manera ascendente por nombre de los personajes.
print('lista de los heroes ordenados por el nombre: ')
superheroes.sort_by_criterion('name')
superheroes.show()
print()

##B) Determinar en que posicion esta The Thing y Rocket Raccoon.
posicion = superheroes.search('The Thing', 'name')
if posicion is not None:
    heroe = superheroes[posicion]
    print(f'el superheroe {heroe["name"]} esta en la posicion: {posicion}')

print()

posicion = superheroes.search('Rocket Raccoon', 'name')
if posicion is not None:
      heroe = superheroes[posicion]
      print(f'el superheroe {heroe["name"]} esta en la posicion: {posicion}')

print()
##C) Listar todos los villanos de la lista
cola_aux = Queue()
tamaño = superheroes.size()
print('Lista de villanos: ')
for i in range(tamaño):
      heroe = superheroes[i]
      if heroe['is_villain'] == True:
            print(f'-{heroe["name"]}')
            #D)Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
            cola_aux.arrive(heroe)
print()
print('villanos que aparecieron antes de 1980: ')
while cola_aux.size() > 0:
      villanos = cola_aux.attention()
      if villanos['first_appearance'] < 1980:
            print(f'-{villanos["name"]}, año: {villanos["first_appearance"]}')
print()

##E)Listar los superheores que comienzan con  Bl, G, My, y W.
print('Lista de heroes que empiezan con Bl, G, My, W: ')
superheroes.filter_start_with(('Bl', 'G', 'My', 'W'))
print()


##F)Listado de personajes ordenado por nombre real de manera ascendente de los personajes
print('lista ordenada por nombre: ')
superheroes.sort_by_criterion('real_name')
superheroes.show()
print()

##G)Listado de superheroes ordenados por fecha de aparación.
print('lista ordenada por año de aparicion: ')
superheroes.sort_by_criterion('first_appearance')
superheroes.show()
print()

##H)Modificar el nombre real de Ant Man a Scott Lang.
print('Cambio de nombre')
buscado = superheroes.search('Ant Man', 'name')
if buscado is not None:
      heroe = superheroes[buscado]
      print(f'Antes: {heroe["real_name"]}')
      heroe["real_name"] = 'Scott Lang'
      print(f'Despues: {heroe["real_name"]}')

print()
##I)Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
print('Heroes con la palabra time-raveling o suit en si biografia: ')
superheroes.filter_contain_on_bio(('time-traveling', 'suit'))
print()

##J)Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
Eliminado = superheroes.delete_value('Electro', 'name')
print(f'Personaje eliminado: {Eliminado["name"]}, Alias: {Eliminado["alias"]}, Nombre Real: {Eliminado["real_name"]}, Biografia: {Eliminado["short_bio"]}, Aparicion: {Eliminado["first_appearance"]}, Villano? {heroe["is_villain"]}')

print()

Eliminado = superheroes.delete_value('Baron Zemo', 'name')
print(f'Personaje Eliminado: {Eliminado["name"]}, Alias: {Eliminado["alias"]}, Nombre Real: {Eliminado["real_name"]}, Biografia: {Eliminado["short_bio"]}, Aparicion: {Eliminado["first_appearance"]}, Villano? {Eliminado["is_villain"]}')

print()
superheroes.show()