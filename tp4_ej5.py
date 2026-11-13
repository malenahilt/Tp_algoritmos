#Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
#rias para poder realizar las siguientes actividades:

#a. eliminar el nodo que contiene la información de Linterna Verde;
#b. mostrar el año de aparición de Wolverine;
#c. cambiar la casa de Dr. Strange a Marvel;
#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#g. mostrar toda la información de Flash y Star-Lord;
#h. listar los superhéroes que comienzan con la letra B, M y S;
#i. determinar cuántos superhéroes hay de cada casa de comic.

from typing import Any, Optional
from lista__ import List
from random import randint

class Superheroes:
   def __init__(self,nom, año_aparicion, casa, biografia):
       self.nom = nom
       self.año_aparicion = año_aparicion
       self.casa = casa
       self.biografia = biografia
    
    
def __str__(self):
        return(f'heroe: {self.nom}, año de aparicion: {self.año_aparicion}, casa: {self.casa}, biografia: {self.biografia}')

def by_name(item):
    return item.nom

def by_casa(item):
    return item.casa

def by_año(item):
    return item.año_aparicion

l = List()
l.add_criterion('nombre', by_name)
l.add_criterion('casa', by_casa)
l.add_criterion('año de aparicion', by_año)

l.append(Superheroes('Batman', 1939, 'DC', 'El caballero de la noche...'))
l.append(Superheroes('Spider-man', 1962, 'Marvel', 'Un joven picado por una araña...'))
l.append(Superheroes('Iron-Man', 1963, 'Marvel', 'Un millonario con armadura...'))
l.append(Superheroes('Wolverine', 1974,'DC','un joven mutado geneticamente...' ))
l.append(Superheroes('Dr.Strange', 1978, 'DC', 'Un neurocirujano sufre un accidente...'))
l.append(Superheroes('Capitana Marvel', 1968, 'Marvel', 'ex piloto de la Fuerza Aérea convertida en una superheroína...'))
l.append(Superheroes('Mujer Maravilla',1941 ,'DC', 'superheroína y princesa guerrera amazona de DC Comics...'))
l.append(Superheroes('Flash', 1940, 'Dc', 'un científico forense que adquirió sus poderes tras ser alcanzado por un rayo '))
l.append(Superheroes('Star-Lord', 1976, 'Marvel', 'Mitad humano y mitad alienígena, carismático líder de los Guardianes de la Galaxia'))
l.append(Superheroes('Linterna Verde', 1959, 'DC', 'protege el sector espacial 2814 usando un anillo que materializa sus pensamientos'))
#a)
print(f'dato eliminado: {l.delete_value("Linterna Verde", "nombre")}')
l.show()
#b)
print()
posicion = l.search('Wolverine', 'nombre')
if posicion is not None:
    heroe = l[posicion]
print(f'heroe encontrado: {heroe.nom}, año de aparicion: {heroe.año_aparicion}')
#c)
cambio_casa = l.search('Dr.Strange', 'nombre')
if cambio_casa is not None:
    heroe = l[cambio_casa]
    print(f'antes: {heroe.nom}, casa: {heroe.casa}')
    heroe.casa = 'Marvel'
    print(f'ahora: {heroe.nom}, casa: {heroe.casa}')


#d)
for heroe in l:
  arm_bio = heroe.biografia
  if 'armadura' in arm_bio or 'traje' in arm_bio:
            print(f'heroe que menciona armadura en su biografia: {heroe.nom}')


#e)
for heroe in l:
    aparicion = heroe.año_aparicion
    if aparicion < 1963:
        print('heroe que aparece antes de 1963:')
        print(f'heroe: {heroe.nom}, casa: {heroe.casa}')


#f)
buscado1 = l.search('Capitana Marvel', 'nombre')
buscado2 = l.search('Mujer Maravilla', 'nombre')
if buscado1 is not None:
    heroe = l[buscado1]
    print(f'el heroe {heroe.nom} pertenece a la casa {heroe.casa}')

if buscado2 is not None:
    heroe = l[buscado2]
    print(f'el heroe {heroe.nom} pertenece a la casa {heroe.casa}')

#g)
buscar1 = l.search('Flash', 'nombre')
buscar2 = l.search('Star-Lord', 'nombre')

if buscar1 is not None:
    heroe = l[buscar1]
    print(f'heroe: {heroe.nom}, año: {heroe.año_aparicion}, casa: {heroe.casa}, biografia: {heroe.biografia}')

if buscar2 is not None:
    heroe = l[buscar2]
    print(f'heroe: {heroe.nom}, año: {heroe.año_aparicion}, casa: {heroe.casa}, biografia: {heroe.biografia}')


#h)
inicio = ('B', 'S', 'M')
for heroe in l:
    if heroe.nom.startswith(inicio):
        print(f'-{heroe.nom}')

#i)
cont_DC = 0
cont_M = 0
for heroe in l:
    cual_casa = heroe.casa
    if cual_casa == 'DC':
        cont_DC += 1
    else:
        cont_M += 1

print(f'la cantidad de heroes en la lista de DC son: {cont_DC}')
print(f'la cantidad de heroes en la lista de la casa de Marvel son: {cont_M}')