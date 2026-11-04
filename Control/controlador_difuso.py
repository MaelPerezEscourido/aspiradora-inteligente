def pertenencia_trapezoidal(valor, a, b, c, d):

    if valor < a or valor > d:
        return 0

    elif b <= valor <= c:
        return 1

    elif valor < b:
        return (valor - a) / (b - a)

    else:
        return (d - valor) / (d - c)

# Conjuntos difusos de velocidad
VELOCIDAD_LENTA = (0, 0, 20, 40)
VELOCIDAD_NORMAL = (20, 40, 60, 80)
VELOCIDAD_RAPIDA = (60, 80, 100, 100)

def aplicar_reglas(suciedad_baja, suciedad_media, suciedad_alta):

    velocidad_lenta = suciedad_alta
    velocidad_normal = suciedad_media
    velocidad_rapida = suciedad_baja

    return velocidad_lenta, velocidad_normal, velocidad_rapida

def recortar_conjunto(valor, conjunto, activacion):
    pertenencia = pertenencia_trapezoidal(valor, *conjunto)

    return min(pertenencia, activacion)

def agregar_conjuntos(valor, lenta, normal, rapida):
    pertenencia_lenta = recortar_conjunto(
        valor, VELOCIDAD_LENTA, lenta
    )

    pertenencia_normal = recortar_conjunto(
        valor, VELOCIDAD_NORMAL, normal
    )

    pertenencia_rapida = recortar_conjunto(
        valor, VELOCIDAD_RAPIDA, rapida
    )

    return max(
        pertenencia_lenta,
        pertenencia_normal,
        pertenencia_rapida
    )

def defuzzificar(lenta, normal, rapida):
    numerador = 0
    denominador = 0

    for velocidad in range(101):
        pertenencia = agregar_conjuntos(
            velocidad, lenta, normal, rapida
        )

        numerador += velocidad * pertenencia
        denominador += pertenencia

    if denominador == 0:
        return 0

    return numerador / denominador