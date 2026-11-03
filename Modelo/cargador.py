class Cargador:

    def __init__(self, zona, x, y):
        self.zona = zona
        self.x = x
        self.y = y

    def esta_robot_en_cargador(self, robot):
        return (
            robot.zona_actual == self.zona
            and robot.x == self.x
            and robot.y == self.y
        )