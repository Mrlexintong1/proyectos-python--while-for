numero = int(input("Ingresa un número entero para calcular su factorial: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}.")