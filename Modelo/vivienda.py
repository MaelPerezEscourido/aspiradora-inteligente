
from Modelo.zona import Zona
from Modelo.cuadrante import Cuadrante


class Vivienda:

    def __init__(self):
        self.zonas = {}

    def agregar_zona(self, nombre, filas, columnas):
        if nombre in self.zonas:
            print(f"La zona {nombre} ya existe.")
            return

        zona = Zona(nombre)

        for y in range(filas):
            for x in range(columnas):
                cuadrante = Cuadrante(
                    x, y, nombre, suciedad=0
                )

                zona.agregar_cuadrante(cuadrante)

        self.zonas[nombre] = zona

    def obtener_cuadrante(self, nombre_zona, x, y):
        if nombre_zona not in self.zonas:
            return None

        for cuadrante in self.zonas[nombre_zona].cuadrantes:
            if cuadrante.x == x and cuadrante.y == y:
                return cuadrante

        return None

    def mostrar_vivienda(self):
        for zona in self.zonas.values():
            print(f"\n--- {zona.nombre.upper()} ---")
            print(f"Suciedad de la zona: {zona.calcular_suciedad():.2f}%")

            for cuadrante in zona.cuadrantes:
                print(cuadrante)

    def obtener_zona(self, nombre):
        return self.zonas.get(nombre)

    def establecer_obstaculo(self, nombre_zona, x, y, obstaculo=True):
        cuadrante = self.obtener_cuadrante(nombre_zona, x, y)

        if cuadrante is None:
            return False

        cuadrante.obstaculo = obstaculo
        return True