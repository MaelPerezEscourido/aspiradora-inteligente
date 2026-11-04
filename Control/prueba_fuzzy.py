from Control.controlador_difuso import (
    pertenencia_trapezoidal,
    aplicar_reglas,
    recortar_conjunto,
    VELOCIDAD_LENTA,
    VELOCIDAD_NORMAL,
    VELOCIDAD_RAPIDA,
    agregar_conjuntos, 
    defuzzificar
)
# Definimos las tres categorías de suciedad
suciedad_baja = (0, 0, 25, 50)
suciedad_media = (25, 40, 60, 75)
suciedad_alta = (50, 75, 100, 100)

# Probamos diferentes porcentajes de suciedad
valores = [0, 20, 40, 50, 60, 80, 100]

for valor in valores:

    baja = pertenencia_trapezoidal(valor, *suciedad_baja)
    media = pertenencia_trapezoidal(valor, *suciedad_media)
    alta = pertenencia_trapezoidal(valor, *suciedad_alta)

    print(f"\nSuciedad: {valor}%")
    print(f"  Baja: {baja:.2f}")
    print(f"  Media: {media:.2f}")
    print(f"  Alta: {alta:.2f}")

print("\n--- PRUEBA DE REGLAS DIFUSAS ---")

baja = pertenencia_trapezoidal(60, *suciedad_baja)
media = pertenencia_trapezoidal(60, *suciedad_media)
alta = pertenencia_trapezoidal(60, *suciedad_alta)

lenta, normal, rapida = aplicar_reglas(baja, media, alta)

print("Activación velocidad lenta:", lenta)
print("Activación velocidad normal:", normal)
print("Activación velocidad rápida:", rapida)

print("\n--- PRUEBA DE RECORTE ---")

print("Velocidad lenta:", recortar_conjunto(30, VELOCIDAD_LENTA, lenta))
print("Velocidad normal:", recortar_conjunto(30, VELOCIDAD_NORMAL, normal))
print("Velocidad rápida:", recortar_conjunto(30, VELOCIDAD_RAPIDA, rapida))

print("\n--- PRUEBA DE AGREGACIÓN ---")

for velocidad in range(0, 101, 10):
    resultado = agregar_conjuntos(
        velocidad, lenta, normal, rapida
    )

    print(f"Velocidad {velocidad}: {resultado:.2f}")

print("\n--- PRUEBA DE DEFUZZIFICACIÓN ---")

velocidad_final = defuzzificar(lenta, normal, rapida)

print("Velocidad final:", round(velocidad_final, 2))