

##Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
##de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
##más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
##las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
#a. obtener la cantidad de Pokémons de un determinado entrenador;
#b. listar los entrenadores que hayan ganado más de tres torneos;
#c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#d. mostrar todos los datos de un entrenador y sus Pokémos;
#e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#(tipo y subtipo);
#g. el promedio de nivel de los Pokémons de un determinado entrenador;
#h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#i. mostrar los entrenadores que tienen Pokémons repetidos;
#j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
#k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

from typing import Any, Optional
from lista__ import List
from random import randint

class List(list):

    __CRITERION_FUNCTION = {}

    def add_criterion(self, criterion_key: str, criterion_function) -> None:
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

    def show(self) -> None:
        for element in self:
            print(element)

    def search(self, search_value: Any, criterion: str = None) -> Optional[int]:
        self.sort_by_criterion(key_criterion=criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        start = 0
        end = len(self) - 1
        middle = (start + end) // 2

        while start <= end:

            if search_criterion is None and not isinstance(self[0], (bool, int, float, str)):
                print('no se pudo determinar criterio de busqueda')
                return None

            value = search_criterion(self[middle]) if search_criterion else self[middle]

            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1

            middle = (start + end) // 2

    def delete_value(self, value, criterion=None) -> Optional[Any]:
        index = self.search(value, criterion)

        return self.pop(index) if index is not None else None

    def sort_by_criterion(self, key_criterion=None) -> None:

        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)

        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, float, str)):
            self.sort()
        else:
            print('no se puede ordenar la lista no se como se debe ordenar')

    def size(self) -> int:
        return len(self)

    def filter_contain_on_bio(self, values):
        for element in self:
            if any(value in element.bio.lower() for value in values):
                print(element)

    def filter_start_with(self, values):
        for element in self:
            if element.name.startswith(values):
                print(element)


class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"  Pokémon: {self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo} | Subtipo: {self.subtipo}"


class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = List()          # lista dentro de la lista de entrenadores
        self.pokemons.add_criterion('pokemon_name', por_nombre_pokemon)
        self.pokemons.add_criterion('pokemon_level', por_nivel)

    def __str__(self):
        return (f"Entrenador: {self.nombre} | Torneos ganados: {self.torneos_ganados} | "
                f"Batallas ganadas: {self.batallas_ganadas} | Batallas perdidas: {self.batallas_perdidas}")



def por_nombre_entrenador(item):
    return item.nombre


def por_torneos(item):
    return item.torneos_ganados


def por_nombre_pokemon(item):
    return item.nombre


def por_nivel(item):
    return item.nivel


def porcentaje_ganadas(entrenador):
    total = entrenador.batallas_ganadas + entrenador.batallas_perdidas
    if total == 0:
        return 0
    return entrenador.batallas_ganadas * 100 / total


def mostrar_entrenador_completo(entrenador):
    print(entrenador)
    entrenador.pokemons.show()


def buscar_entrenador(entrenadores, nombre):
    """Devuelve el entrenador con ese nombre o None."""
    pos = entrenadores.search(nombre, 'trainer_name')
    return entrenadores[pos] if pos is not None else None


def tiene_pokemon(entrenador, nombre_pokemon):
    """Devuelve el Pokémon si el entrenador lo tiene, sino None."""
    pos = entrenador.pokemons.search(nombre_pokemon, 'pokemon_name')
    return entrenador.pokemons[pos] if pos is not None else None


# a. cantidad de Pokémons de un entrenador
def cantidad_pokemons(entrenadores, nombre):
    entrenador = buscar_entrenador(entrenadores, nombre)
    if entrenador is None:
        return None
    return entrenador.pokemons.size()


# b. entrenadores que ganaron más de tres torneos
def entrenadores_mas_de_tres_torneos(entrenadores):
    for entrenador in entrenadores:
        if entrenador.torneos_ganados > 3:
            print(entrenador)


# c. Pokémon de mayor nivel del entrenador con más torneos ganados
def pokemon_mayor_nivel_del_mayor_campeon(entrenadores):
    if entrenadores.size() == 0:
        return None, None
    entrenadores.sort_by_criterion('tournaments')
    campeon = entrenadores[-1]                      # el último tiene más torneos
    if campeon.pokemons.size() == 0:
        return campeon, None
    campeon.pokemons.sort_by_criterion('pokemon_level')
    return campeon, campeon.pokemons[-1]            # el último tiene mayor nivel


# d. mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(entrenadores, nombre):
    entrenador = buscar_entrenador(entrenadores, nombre)
    if entrenador is None:
        print('El entrenador no existe')
    else:
        mostrar_entrenador_completo(entrenador)


# e. entrenadores con porcentaje de batallas ganadas mayor al 79 %
def entrenadores_porcentaje_mayor_79(entrenadores):
    for entrenador in entrenadores:
        if porcentaje_ganadas(entrenador) > 79:
            print(f"{entrenador} | Porcentaje de victorias: {porcentaje_ganadas(entrenador):.2f} %")


# f. entrenadores con Pokémons tipo fuego/planta o agua/volador (tipo/subtipo)
def entrenadores_fuego_planta_o_agua_volador(entrenadores):
    for entrenador in entrenadores:
        cumple = False
        for pokemon in entrenador.pokemons:
            tipo = pokemon.tipo.lower()
            subtipo = pokemon.subtipo.lower()
            if (tipo == 'fuego' and subtipo == 'planta') or (tipo == 'agua' and subtipo == 'volador'):
                cumple = True
        if cumple:
            print(entrenador)


# g. promedio de nivel de los Pokémons de un entrenador
def promedio_nivel(entrenadores, nombre):
    entrenador = buscar_entrenador(entrenadores, nombre)
    if entrenador is None or entrenador.pokemons.size() == 0:
        return None
    suma = 0
    for pokemon in entrenador.pokemons:
        suma += pokemon.nivel
    return suma / entrenador.pokemons.size()


# h. cuántos entrenadores tienen un determinado Pokémon
def cantidad_entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    cantidad = 0
    for entrenador in entrenadores:
        if tiene_pokemon(entrenador, nombre_pokemon) is not None:
            cantidad += 1
    return cantidad


# i. entrenadores con Pokémons repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    for entrenador in entrenadores:
        entrenador.pokemons.sort_by_criterion('pokemon_name')
        repetido = False
        for i in range(1, entrenador.pokemons.size()):
            if entrenador.pokemons[i].nombre == entrenador.pokemons[i - 1].nombre:
                repetido = True
        if repetido:
            print(entrenador)


# j. entrenadores que tengan Tyrantrum, Terrakion o Wingull
def entrenadores_con_alguno_de(entrenadores, nombres=('Tyrantrum', 'Terrakion', 'Wingull')):
    for entrenador in entrenadores:
        tiene_alguno = False
        for nombre in nombres:
            if tiene_pokemon(entrenador, nombre) is not None:
                tiene_alguno = True
        if tiene_alguno:
            print(entrenador)


# k. determinar si el entrenador X tiene al Pokémon Y y mostrar los datos de ambos
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    entrenador = buscar_entrenador(entrenadores, nombre_entrenador)
    if entrenador is None:
        print('El entrenador no existe')
        return
    pokemon = tiene_pokemon(entrenador, nombre_pokemon)
    if pokemon is None:
        print(f'{entrenador.nombre} no tiene a {nombre_pokemon}')
    else:
        print(f'{entrenador.nombre} tiene a {pokemon.nombre}')
        print(entrenador)
        print(pokemon)



def cargar_datos():
    entrenadores = List()
    entrenadores.add_criterion('trainer_name', por_nombre_entrenador)
    entrenadores.add_criterion('tournaments', por_torneos)

    datos = [
        (Entrenador('Ash', 5, 20, 95), [
            Pokemon('Pikachu', 60, 'Electrico', 'Ninguno'),
            Pokemon('Charizard', 75, 'Fuego', 'Volador'),
            Pokemon('Wingull', 30, 'Agua', 'Volador'),
        ]),
        (Entrenador('Misty', 2, 40, 60), [
            Pokemon('Starmie', 55, 'Agua', 'Psiquico'),
            Pokemon('Gyarados', 62, 'Agua', 'Volador'),
            Pokemon('Starmie', 40, 'Agua', 'Psiquico'),
        ]),
        (Entrenador('Brock', 4, 25, 80), [
            Pokemon('Onix', 50, 'Roca', 'Tierra'),
            Pokemon('Tyrantrum', 58, 'Roca', 'Dragon'),
        ]),
        (Entrenador('Cynthia', 8, 10, 190), [
            Pokemon('Garchomp', 90, 'Dragon', 'Tierra'),
            Pokemon('Terrakion', 85, 'Roca', 'Lucha'),
            Pokemon('Spiritomb', 80, 'Fantasma', 'Siniestro'),
        ]),
        (Entrenador('Gary', 1, 30, 40), [
            Pokemon('Blastoise', 66, 'Agua', 'Ninguno'),
            Pokemon('Arcanine', 61, 'Fuego', 'Ninguno'),
        ]),
    ]

    for entrenador, pokemons in datos:
        for pokemon in pokemons:
            entrenador.pokemons.append(pokemon)
        entrenadores.append(entrenador)

    return entrenadores



def main():
    entrenadores = cargar_datos()

    menu = """
--- MENÚ ---
a. Cantidad de Pokémons de un entrenador
b. Entrenadores con más de 3 torneos ganados
c. Pokémon de mayor nivel del entrenador con más torneos
d. Datos de un entrenador y sus Pokémons
e. Entrenadores con más del 79 % de batallas ganadas
f. Entrenadores con Pokémons fuego/planta o agua/volador
g. Promedio de nivel de los Pokémons de un entrenador
h. Cantidad de entrenadores que tienen un Pokémon
i. Entrenadores con Pokémons repetidos
j. Entrenadores con Tyrantrum, Terrakion o Wingull
k. ¿El entrenador X tiene al Pokémon Y?
0. Salir
"""

    opcion = ''
    while opcion != '0':
        print(menu)
        opcion = input('Opción: ').strip().lower()

        if opcion == 'a':
            nombre = input('Entrenador: ').strip().title()
            cant = cantidad_pokemons(entrenadores, nombre)
            print('El entrenador no existe' if cant is None else f'{nombre} tiene {cant} Pokémons')

        elif opcion == 'b':
            entrenadores_mas_de_tres_torneos(entrenadores)

        elif opcion == 'c':
            campeon, pokemon = pokemon_mayor_nivel_del_mayor_campeon(entrenadores)
            if campeon is None:
                print('No hay entrenadores cargados')
            else:
                print(f'Entrenador con más torneos: {campeon}')
                print(pokemon if pokemon else 'No tiene Pokémons')

        elif opcion == 'd':
            nombre = input('Entrenador: ').strip().title()
            mostrar_datos_entrenador(entrenadores, nombre)

        elif opcion == 'e':
            entrenadores_porcentaje_mayor_79(entrenadores)

        elif opcion == 'f':
            entrenadores_fuego_planta_o_agua_volador(entrenadores)

        elif opcion == 'g':
            nombre = input('Entrenador: ').strip().title()
            prom = promedio_nivel(entrenadores, nombre)
            if prom is None:
                print('El entrenador no existe o no tiene Pokémons')
            else:
                print(f'Promedio de nivel de {nombre}: {prom:.2f}')

        elif opcion == 'h':
            nombre_pokemon = input('Pokémon: ').strip().title()
            cant = cantidad_entrenadores_con_pokemon(entrenadores, nombre_pokemon)
            print(f'{cant} entrenador(es) tienen a {nombre_pokemon}')

        elif opcion == 'i':
            entrenadores_con_pokemons_repetidos(entrenadores)

        elif opcion == 'j':
            entrenadores_con_alguno_de(entrenadores)

        elif opcion == 'k':
            nombre_entrenador = input('Entrenador: ').strip().title()
            nombre_pokemon = input('Pokémon: ').strip().title()
            entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon)


if __name__ == '__main__':
    main()