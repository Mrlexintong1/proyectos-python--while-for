temperaturas = []

while True:
    try:
        temp = float(input("Ingrese temperatura en °C (-273 para finalizar): "))
        if temp == -273:
            break
        temperaturas.append(temp)
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")

if temperaturas:
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"El promedio de temperaturas es: {promedio:.2f}°C")
else:
    print("No se ingresaron temperaturas válidas.")