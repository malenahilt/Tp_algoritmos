from lista__ import List
from random import randint


##Dada una lista de números enteros eliminar de estas los números primos.
l = List()
for i in range(10):
    l.append(int(randint(1, 10)))
print()
l.show()

tamaño_lista = l.size() - 1
while tamaño_lista >= 0:
    num = l[tamaño_lista]
    if num % 2 != 0 or num == 2:
       l.delete_value(num)
    tamaño_lista-=1     

print('lista sin numeros primos')
l.show()
