inicio = int(input("Ingresa el primer número entero: "))
fin = int(input("Ingresa el segundo número entero: "))

if inicio < fin:
    for numero in range(inicio, fin + 1):
        print(numero)
else:
    for numero in range(inicio, fin - 1, -1):
        print(numero)