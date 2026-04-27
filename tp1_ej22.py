def usar_la_fuerza(mochila, posicion=0):
    if posicion >= len(mochila):
        print("La mochila está vacía... no había sable de luz.")
        return  False, 0
    
    objetos = mochila[posicion]
    print(f"  Objetos {posicion + 1} sacado: {objetos}")

    if objetos == "sable de luz":
        print("El Jedi encontró su sable de luz")
        return True, posicion + 1
    
    encontrado, cantidad = usar_la_fuerza(mochila, posicion + 1)
    return encontrado, cantidad

mochila = [
    "objeto A",
    "objeto B",
    "objeto C",
    "objeto D",
    "sable de luz",
    "objeto E"
]
 
encontrado, cantidad = usar_la_fuerza(mochila)
print()
if encontrado:
    print(f"Sable de luz encontrado después de sacar {cantidad} objetos.")
else:
    print(f"No había sable de luz. Se sacaron {len(mochila)} objetos en total.")