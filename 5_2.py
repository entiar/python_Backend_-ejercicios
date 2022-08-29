#Escribe una función que pueda decirte si un número (número entero) es primo o no.
def primo(k):
    if k > 1:
        for i in range(2, int(k/2)+1):
             if (k % i) == 0:
                print("No es un número primo")
                break
        else:
            print("Es un número primo")

    else:
        print("No es un numero primero")
        
primo(13)
