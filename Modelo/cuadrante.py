class Cuadrante:

    def __init__(self, x, y, zona, suciedad=0, obstaculo=False):
        self.x = x
        self.y = y
        self.zona = zona
        self.suciedad = suciedad
        self.obstaculo = obstaculo

    def limpiar(self, cantidad):
        if not self.obstaculo:
            self.suciedad = max(0, self.suciedad - cantidad)

    def esta_limpio(self):
        return self.suciedad == 0

    def __str__(self):
        if self.obstaculo:
            return "OBSTACULO"

        return f"Cuadrante ({self.x}, {self.y}) - Suciedad: {self.suciedad}%"
