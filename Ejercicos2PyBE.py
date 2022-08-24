#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
numeros = range(1,101)
orden = sorted(numeros, reverse=True)
for valor in orden:
    print(valor)
