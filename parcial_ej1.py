

lista = [
  {'name': 'Hulk'} ,
  {'name': 'Black Widow'},
  {'name': 'Iron Man'},
  {'name': 'Ant Man'},
  {'name': 'Black Panther'},
  {'name': 'Captain America'},
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

##funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
##funcion recursiva para listar los superheroes de la lista.

def buscar_Personaje(lista, indice = 0):
    if indice == len(lista):            ##caso de no encontrarlo y llegamos al final de la lista.
        return 0
    if lista[indice] == 'Capitan America':
        return 
    
    