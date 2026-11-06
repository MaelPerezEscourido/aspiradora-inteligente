from Modelo.fuzzy.controlador_fuzzy import ControladorFuzzy
import random

class Controlador:

    def __init__(self):
        self.controlador_fuzzy = ControladorFuzzy()

    def actualizar_velocidad(self, robot, vivienda):

        cuadrante = robot.obtener_cuadrante_actual(vivienda)

        if cuadrante is None or cuadrante.obstaculo:
            return False

        suciedad = cuadrante.suciedad
        bateria = robot.obtener_bateria()

        velocidad = self.controlador_fuzzy.calcular_velocidad(
            suciedad,
            bateria
        )

        robot.establecer_velocidad(velocidad)

        return velocidad

    def limpiar_cuadrante(self, robot, vivienda):

        cuadrante = robot.obtener_cuadrante_actual(vivienda)

        if cuadrante is None or cuadrante.obstaculo:
            return False

        if cuadrante.esta_limpio():
            return False

        # Calcular la velocidad según suciedad y batería
        self.actualizar_velocidad(robot, vivienda)

        # Limpiar el cuadrante
        cuadrante.limpiar(10)

        # Consumir batería
        robot.consumir_bateria(1)

        return True

    def limpiar_hasta_terminar(self, robot, vivienda):

        cuadrante = robot.obtener_cuadrante_actual(vivienda)

        if cuadrante is None or cuadrante.obstaculo:
            return

        while not cuadrante.esta_limpio() and robot.obtener_bateria() > 0:

            self.limpiar_cuadrante(robot, vivienda)

            print(
                f"Suciedad: {cuadrante.suciedad}% | "
                f"Batería: {robot.bateria}% | "
                f"Velocidad: {robot.velocidad:.2f}%"
            )

    def mover_robot(self, robot, vivienda, x, y):

        cuadrante = vivienda.obtener_cuadrante(
            robot.zona_actual, x, y
        )

        if cuadrante is None or cuadrante.obstaculo:
            return False

        robot.moverse(robot.zona_actual, x, y)

        return True

    def mover_aleatorio(self, robot, vivienda):

        x = robot.x
        y = robot.y

        # Posibles movimientos: derecha, izquierda, abajo y arriba
        posiciones = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        vecinos_accesibles = []

        # Comprobar qué posiciones son válidas
        for nueva_x, nueva_y in posiciones:

            cuadrante = vivienda.obtener_cuadrante(
                robot.zona_actual, nueva_x, nueva_y
            )

            if cuadrante is not None and not cuadrante.obstaculo:
                vecinos_accesibles.append((nueva_x, nueva_y))

        # Si no hay vecinos accesibles, no se mueve
        if not vecinos_accesibles:
            return False

        # Elegir aleatoriamente un vecino
        nueva_x, nueva_y = random.choice(vecinos_accesibles)

        # Mover el robot
        self.mover_robot(robot, vivienda, nueva_x, nueva_y)

        return True

    def limpiar_zona(self, robot, vivienda):

        visitados = set()
        camino = []

        while robot.obtener_bateria() > 0:

            posicion = (robot.x, robot.y)

            # Limpiar el cuadrante actual
            if posicion not in visitados:

                visitados.add(posicion)
                camino.append(posicion)

                print(f"\nRobot en cuadrante {posicion}")

                self.limpiar_hasta_terminar(robot, vivienda)

            # Si se agota la batería, detenerse
            if robot.obtener_bateria() <= 0:
                print("El robot se ha quedado sin batería.")
                break

            # Buscar vecinos accesibles no visitados
            x, y = robot.x, robot.y

            posiciones = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1)
            ]

            vecinos = []

            for nueva_x, nueva_y in posiciones:

                cuadrante = vivienda.obtener_cuadrante(
                    robot.zona_actual, nueva_x, nueva_y
                )

                if (cuadrante is not None
                        and not cuadrante.obstaculo
                        and (nueva_x, nueva_y) not in visitados):

                    vecinos.append((nueva_x, nueva_y))

            if vecinos:
                # Elegir aleatoriamente un vecino sin visitar
                nueva_x, nueva_y = random.choice(vecinos)

                self.mover_robot(robot, vivienda, nueva_x, nueva_y)

                print(f"Moviendo a ({nueva_x}, {nueva_y})")

            else:
                # Si no quedan vecinos nuevos, retroceder
                camino.pop()

                if not camino:
                    print("\nTodos los cuadrantes accesibles han sido visitados.")
                    break

                anterior_x, anterior_y = camino[-1]

                self.mover_robot(robot, vivienda, anterior_x, anterior_y)

                print(f"Retrocediendo a ({anterior_x}, {anterior_y})")