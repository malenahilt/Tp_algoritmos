##funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
##funcion recursiva para listar los superheroes de la lista.

lista = [
  {'name': 'Hulk'} ,
  {'name': 'Black Widow'},
  {'name': 'Iron Man'},
  {'name': 'Ant Man'},
  {'name': 'Black Panther'},
  {'name': 'Capitan America'},
  {'name': 'Deadpool'},
  {'name': 'Gamora'},
  {'name': 'Groot'},
  {'name': 'Hawkaye'},
  {'name': 'Loki'},
  {'name': 'Nebula'},
  {'name': 'Rocket Raccoon'},
  {'name': 'SpiderMan'},
  {'name': 'Thor'},  
]

##1)
def Cap_America(lista,indice = 0):
    if indice == len(lista):
        return None
    elif lista['name'] == 'Capitan America':
        return True
    else:
        return Cap_America(lista, indice + 1)

print(f'el Capitan America fue encontrado')

##2)funcion recursiva para listar los superheroes de la lista.

def listar_heroes(lista, indice = 0):
    if indice == len(lista):
        return None
    else:
        print(f'-{lista[indice]["name"]}')
        return listar_heroes(lista, indice + 1)

listar_heroes(lista)
    
    

