from skfuzzy import control as ctrl

from .reglas import REGLAS


class ControladorFuzzy:

    def __init__(self):
        sistema = ctrl.ControlSystem(REGLAS)
        self.simulador = ctrl.ControlSystemSimulation(sistema)

    def calcular_velocidad(self, nivel_suciedad, nivel_bateria):

        if not 0 <= nivel_suciedad <= 100:
            raise ValueError(
                "El nivel de suciedad debe estar entre 0 y 100"
            )

        if not 0 <= nivel_bateria <= 100:
            raise ValueError(
                "El nivel de batería debe estar entre 0 y 100"
            )

        self.simulador.input["suciedad"] = nivel_suciedad
        self.simulador.input["bateria"] = nivel_bateria

        self.simulador.compute()

        return self.simulador.output["velocidad"]