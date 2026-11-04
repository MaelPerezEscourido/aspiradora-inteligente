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


REGLAS = [
    regla_1,
    regla_2,
    regla_3,
    regla_4,
    regla_5,
    regla_6,
    regla_7,
    regla_8,
    regla_9
]