"""Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados 
por comas."""
paises = input("Introduzca nombres de paises: ")
paisesF = sorted(list(set(paises.split())))
print(paisesF)
