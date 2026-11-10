import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Entrada: suciedad entre 0 y 100
suciedad = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "suciedad"
)

# Entrada: batería entre 0 y 100 %
bateria = ctrl.Antecedent(
    np.arange(0, 101, 1),
    "bateria"
)

# Salida: velocidad entre 0 y 100 %
velocidad = ctrl.Consequent(
    np.arange(0, 101, 1),
    "velocidad"
)

potencia = ctrl.Consequent(
    np.arange(0, 101, 1),
    "potencia"
)



# Conjuntos fuzzy de suciedad
suciedad["baja"] = fuzz.trimf(
    suciedad.universe,
    [1, 1, 50]
)

suciedad["media"] = fuzz.trimf(
    suciedad.universe,
    [20, 50, 80]
)

suciedad["alta"] = fuzz.trimf(
    suciedad.universe,
    [50, 100, 100]
)


bateria["baja"] = fuzz.trimf(
    bateria.universe,
    [0, 0, 50]
)

bateria["media"] = fuzz.trimf(
    bateria.universe,
    [20, 50, 80]
)

bateria["alta"] = fuzz.trimf(
    bateria.universe,
    [50, 100, 100]
)



# Conjuntos fuzzy de velocidad
velocidad["lenta"] = fuzz.trimf(
    velocidad.universe,
    [0, 0, 50]
)

velocidad["media"] = fuzz.trimf(
    velocidad.universe,
    [20, 50, 80]
)

velocidad["rapida"] = fuzz.trimf(
    velocidad.universe,
    [50, 100, 100]
)

# Conjuntos fuzzy de potencia
potencia["baja"] = fuzz.trimf(
    potencia.universe,
    [0, 0, 50]
)   

potencia["media"] = fuzz.trimf(
    potencia.universe,
    [20, 50, 80]
)

potencia["alta"] = fuzz.trimf(
    potencia.universe,
    [50, 100, 100]
)