class Robot:

    def __init__(self, bateria=100):
        self.bateria = max(0, min(100, bateria))
        self.zona_actual = None
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.velocidad = 0

    def actualizar_posicion(self, zona, x, y):
        self.zona_actual = zona
        self.x = x
        self.y = y

        self.pos_x = float(x)
        self.pos_y = float(y)

    def consumir_bateria(self, cantidad):
        if cantidad < 0:
            return False

        self.bateria = max(0, self.bateria - cantidad)
        return True

    def obtener_bateria(self):
        return self.bateria

    def recargar_bateria(self):
        self.bateria = 100

    def moverse(self, zona, x, y):
        self.actualizar_posicion(zona, x, y)

    def obtener_cuadrante_actual(self, vivienda):
        return vivienda.obtener_cuadrante(
            self.zona_actual,
            self.x,
            self.y
        )
    def establecer_velocidad(self, velocidad):
        if velocidad < 0:
            return False

        self.velocidad = velocidad
        return True