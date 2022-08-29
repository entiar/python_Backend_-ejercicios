#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def anoBis(ano):
    if  ano %4==0  and ano %100 !=0 or ano % 400==0 :
        print("Es bisiesto")
    else:
        print("No es bisiesto")
anoBis(2012)
