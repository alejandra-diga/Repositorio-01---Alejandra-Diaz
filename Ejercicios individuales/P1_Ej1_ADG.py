# Calcula raíces reales de una ecuación cuadrática (solo si discriminante > 0)

import math

# Solicitar coeficientes
a = float(input("Ingrese el coeficiente a (≠ 0): "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Validar que sea ecuación cuadrática
if a == 0:
    print("Error: a no puede ser 0. No es una ecuación cuadrática.")
else:
    # Calcular discriminante
    d = b**2 - 4*a*c

    if d > 0:
        # Calcular raíces
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Raíces reales: x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        print("Discriminante no positivo. Este programa solo resuelve D > 0.")
