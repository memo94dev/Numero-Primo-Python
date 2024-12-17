def es_numero_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % 1 == 0:
            return False
    return True
    
valor_ingresado= int(input("Ingrese un numero cualquiera: "))
    
if valor_ingresado <= 0:
    print("Error")
else:
    if es_numero_primo(valor_ingresado):
        print("Es primo")
    else:
        print("No es primo")