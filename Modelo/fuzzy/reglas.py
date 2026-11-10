from skfuzzy import control as ctrl

from .variables import suciedad, bateria, velocidad


regla_1 = ctrl.Rule(
    suciedad["baja"] & bateria["alta"],
    velocidad["rapida"]
)

regla_2 = ctrl.Rule(
    suciedad["media"] & bateria["alta"],
    velocidad["media"]
)

regla_3 = ctrl.Rule(
    suciedad["alta"] & bateria["alta"],
    velocidad["lenta"]
)

regla_4 = ctrl.Rule(
    suciedad["baja"] & bateria["media"],
    velocidad["media"]
)

regla_5 = ctrl.Rule(
    suciedad["media"] & bateria["media"],
    velocidad["media"]
)

regla_6 = ctrl.Rule(
    suciedad["alta"] & bateria["media"],
    velocidad["lenta"]
)

regla_7 = ctrl.Rule(
    suciedad["baja"] & bateria["baja"],
    velocidad["lenta"]
)

regla_8 = ctrl.Rule(
    suciedad["media"] & bateria["baja"],
    velocidad["lenta"]
)

regla_9 = ctrl.Rule(
    suciedad["alta"] & bateria["baja"],
    velocidad["lenta"]
)

# Reglas de potencia de aspiración

regla_10 = ctrl.Rule(
    suciedad["baja"] & bateria["alta"],
    potencia["baja"]
)

regla_11 = ctrl.Rule(
    suciedad["media"] & bateria["alta"],
    potencia["media"]
)

regla_12 = ctrl.Rule(
    suciedad["alta"] & bateria["alta"],
    potencia["alta"]
)

regla_13 = ctrl.Rule(
    suciedad["baja"] & bateria["media"],
    potencia["baja"]
)

regla_14 = ctrl.Rule(
    suciedad["media"] & bateria["media"],
    potencia["media"]
)

regla_15 = ctrl.Rule(
    suciedad["alta"] & bateria["media"],
    potencia["alta"]
)

regla_16 = ctrl.Rule(
    suciedad["baja"] & bateria["baja"],
    potencia["baja"]
)

regla_17 = ctrl.Rule(
    suciedad["media"] & bateria["baja"],
    potencia["baja"]
)

regla_18 = ctrl.Rule(
    suciedad["alta"] & bateria["baja"],
    potencia["media"]
)


REGLAS = [
    regla_1,
    regla_2,
    regla_3,
    regla_4,
    regla_5,
    regla_6,
    regla_7,
    regla_8,
    regla_9,
    regla_10,
    regla_11,
    regla_12,
    regla_13,
    regla_14,
    regla_15,
    regla_16,
    regla_17,
    regla_18
]