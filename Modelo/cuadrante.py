class Cuadrante:

    def __init__(self, x, y, zona, suciedad=0, obstaculo=False):
        self.x = x
        self.y = y
        self.zona = zona
        self.suciedad = suciedad
        self.obstaculo = obstaculo

    def limpiar(self, cantidad):
        if self.obstaculo or cantidad < 0:
            return False

        self.establecer_suciedad(self.suciedad - cantidad)
        return True

    def esta_limpio(self):
        return self.suciedad == 0

    def __str__(self):
        if self.obstaculo:
            return "OBSTACULO"

        return f"Cuadrante ({self.x}, {self.y}) - Suciedad: {self.suciedad}%"

    def establecer_suciedad(self, cantidad):
        if self.obstaculo:
            return False

        self.suciedad = max(0, min(100, cantidad))
        return True