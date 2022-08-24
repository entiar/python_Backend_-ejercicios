#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
minN = int(input('Ingrese el número inicial: '))
maxN = int(input('Ingrese el número final: '))
rango = range(minN, (maxN+1))
mt = []
for valor in rango:
    if valor%2 != 0:
        mt.append(valor)
print(mt) 
