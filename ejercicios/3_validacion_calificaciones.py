calificaciones = []

while len(calificaciones) < 15:
    try:
        calificacion = float(input(f"Ingrese la calificación {len(calificaciones)+1} (0 a 5): "))
        if 0 <= calificacion <= 5:
            calificaciones.append(calificacion)
        else:
            print("Valor inválido. Intenta nuevamente.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")