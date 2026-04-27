
convr_valores = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000 
        }

def conversion_decimal(romano, posicion=0):
if posicion >= len(romano):
    return 0

valor_actual = convr_valores[romano[posicion]]

if posicion + 1 < len(romano):
    valor_siguiente = convr_valores[romano[posicion + 1]]

## suma y resta

if valor_actual < valor_siguiente:
    return -valor_actual + valor_actual (romano, posicion +1)

    return valor_actual + valor_actual (romano, posicion + 1)

numero_romano = input ('ingresa el numero romano: ')
resultado = conversion_decimal (numero_romao, 0)
print (f'{numero_romano} en decimal es {resultado}')