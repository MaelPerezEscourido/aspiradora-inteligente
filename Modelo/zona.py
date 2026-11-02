
from Modelo.cuadrante import Cuadrante


class Zona:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuadrantes = []

    def agregar_cuadrante(self, cuadrante):
        self.cuadrantes.append(cuadrante)

    def calcular_suciedad(self):
        if not self.cuadrantes:
            return 0

        cuadrantes_accesibles = []

        for cuadrante in self.cuadrantes:
            if not cuadrante.obstaculo:
                cuadrantes_accesibles.append(cuadrante)

        if not cuadrantes_accesibles:
            return 0

        total = 0

        for cuadrante in cuadrantes_accesibles:
            total += cuadrante.suciedad

        return total / len(cuadrantes_accesibles)

    def obtener_cuadrante_mas_sucio(self):
        candidatos = []

        for cuadrante in self.cuadrantes:
            if not cuadrante.obstaculo and not cuadrante.esta_limpio():
                candidatos.append(cuadrante)

        if not candidatos:
            return None

        return max(candidatos, key=lambda cuadrante: cuadrante.suciedad)

    def esta_limpia(self):
        return self.calcular_suciedad() == 0
