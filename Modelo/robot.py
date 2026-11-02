class Robot:

    def __init__(self, bateria=100):
        self.bateria = bateria
        self.zona_actual = None
        self.x = 0
        self.y = 0
        self.velocidad = 0

    def actualizar_posicion(self, zona, x, y):
        self.zona_actual = zona
        self.x = x
        self.y = y

    def consumir_bateria(self, cantidad):
        self.bateria = max(0, self.bateria - cantidad)

    def obtener_bateria(self):
        return self.bateria