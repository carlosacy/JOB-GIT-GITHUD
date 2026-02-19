lista=[1,2,3,4,5,9,89]
print(f'n\la longitud de la lista es: {len(lista)}')

suma=0
for i in range(len(lista)):
    suma+=lista[i]
print(f'n\la suma de los elementos de la lista es: {suma}')


multiplicacion=1
for i in range(len(lista)):
    multiplicacion*=lista[i]
print(f'n\la multiplicacion de los elementos de la lista es: {multiplicacion}')