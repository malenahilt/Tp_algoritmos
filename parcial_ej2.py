from lista__ import List
from lista_heroes import superheroes
from cola import Queue

class Heroes:
    def __init__(self,name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name= real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return (f'{self.name}-{self.alias}-{self.real_name}-{self.first_appearance}-{self.is_villain}')
    
    
def by_name(item):
    return item['name']

def by_real_name(item):
    return item['real_name']

def by_first_appearance(item):
    return item['first_appearance']


superheroes = List(superheroes)
superheroes.add_criterion('name', by_name)
superheroes.add_criterion('real name', by_real_name)
superheroes.add_criterion('first appearance', by_first_appearance)
superheroes.show()
print()
##a)Listado ordenado de manera ascendente por nombre de los personajes.
superheroes.sort_by_criterion('name')
superheroes.show()
print()


##b)Determinar en que posicion esta The Thing y Rocket Raccoon.
posicion = superheroes.search('The Thing', 'name')
if posicion is not None:
    heroe = superheroes[posicion]
    print(f'heroe {heroe["name"]} encontrado en la posicion {posicion}')

posicion = superheroes.search('Rocket Raccoon', 'name')
if posicion is not None:
    heroe = superheroes[posicion]
    print(f'heroe {heroe["name"]} encontrado en la posicion {posicion}')

##c)Listar todos los villanos de la lista.
cola_aux = Queue()
tamaño = superheroes.size()
print('lista de villanos: ')
for i in range(tamaño):
    heroe = superheroes[i]
    if heroe['is_villain'] == True:
        print(f'-villano: {heroe["name"]}')
        ##d)Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980
        cola_aux.arrive(heroe)
print()
while cola_aux.size() > 0:
    villanos = cola_aux.attention()
    if villanos['first_appearance'] < 1980:
        print(f'-villanos que aparecieron antes de 1980: {villanos ["name"]}')

##e)Listar los superheores que comienzan con  Bl, G, My, y W.
Iniciales = ['Bl', 'G', 'My', 'W']
for i in range(tamaño):                                 ##no pude hacerlo con la funcion filter_start_with por un error
    heroe = superheroes[i]                              ##de 'dict object has no attribute name' asi que lo hice con dos for.
    for letra in Iniciales:
        if heroe['name'].startswith(letra):
            print(f'-heroe {heroe["name"]}')

##f)Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
print()
superheroes.sort_by_criterion('real_name')
superheroes.show()
print()

##g)Listado de superheroes ordenados por fecha de aparación.
superheroes.sort_by_criterion('first_appearance')
superheroes.show()
print()

##h)Modificar el nombre real de Ant Man a Scott Lang.
buscado = superheroes.search('Ant Man', 'name')
if buscado is not None:
    heroe = superheroes[buscado]
    print(f'antes: {heroe["real_name"]}')
    heroe["real_name"] = 'Scott Lang'
    print(f'despues: {heroe["real_name"]}')

##i)Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
for heroe in superheroes:
    biografia = heroe["short_bio"]
    if ('time-traveling' in biografia) or ('suit' in biografia):
     print(f'heroe: {heroe["name"]}')

##j)Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista
elminar = superheroes.delete_value('Electro', 'name')
print(f'-eliminado: {elminar["name"]}')

elminar2= superheroes.delete_value('Baron Zemo', 'name')
print(f'-eliminado: {elminar2["name"]}')





