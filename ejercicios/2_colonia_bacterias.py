a = 4
b = 10
dias = 0

while a < b:
    a *= 1.03
    b *= 1.015
    dias += 1

print(f"La colonia A superará o igualará a la colonia B en {dias} días.")