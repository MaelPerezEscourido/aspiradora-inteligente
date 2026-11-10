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

        if robot.obtener_bateria() <= 0:
            return False

        # Calcular velocidad mediante lógica difusa
        velocidad = self.actualizar_velocidad(robot, vivienda)

        # Calcular consumo energético según la velocidad
        consumo = 0.5 + (velocidad / 100)

        # Comprobar que existe batería suficiente
        if robot.obtener_bateria() < consumo:
            return False

        # Limpiar el cuadrante
        cuadrante.limpiar(10)

        # Consumir batería según la velocidad calculada
        robot.consumir_bateria(consumo)

        return True

    def limpiar_hasta_terminar(self, robot, vivienda):

        cuadrante = robot.obtener_cuadrante_actual(vivienda)

        if cuadrante is None or cuadrante.obstaculo:
            return False

        while not cuadrante.esta_limpio() and robot.obtener_bateria() > 0:

            # Intentar realizar un paso de limpieza
            resultado = self.limpiar_cuadrante(robot, vivienda)

            # Si no se puede limpiar, detener el bucle
            if not resultado:
                print("No hay batería suficiente para seguir limpiando.")
                return False

            print(
                f"Suciedad: {cuadrante.suciedad}% | "
                f"Batería: {robot.bateria:.2f}% | "
                f"Velocidad: {robot.velocidad:.2f}%"
            )

        return cuadrante.esta_limpio()

    def mover_robot(self, robot, vivienda, x, y):

        consumo_movimiento = 0.5

        # Comprobar que el destino es un vecino
        distancia = abs(robot.x - x) + abs(robot.y - y)

        if distancia != 1:
            return False

        # Comprobar que no hay obstáculos
        cuadrante = vivienda.obtener_cuadrante(
            robot.zona_actual, x, y
        )

        if cuadrante is None or cuadrante.obstaculo:
            return False

        # Comprobar batería
        if robot.obtener_bateria() < consumo_movimiento:
            return False

        # Guardar posición inicial
        inicio_x = robot.pos_x
        inicio_y = robot.pos_y

        # Movimiento progresivo en cuatro pasos
        for paso in range(1, 5):

            progreso = paso / 4

            robot.pos_x = inicio_x + (x - inicio_x) * progreso
            robot.pos_y = inicio_y + (y - inicio_y) * progreso

            print(
                f"Posición: ({robot.pos_x:.2f}, "
                f"{robot.pos_y:.2f})"
            )

        # Consumir batería una vez por desplazamiento
        robot.consumir_bateria(consumo_movimiento)

        # Actualizar el cuadrante al finalizar
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

                if self.mover_robot(robot, vivienda, nueva_x, nueva_y):
                    print(f"Moviendo a ({nueva_x}, {nueva_y})")
                else:
                    print("No se puede continuar el recorrido.")
                    break
            else:
                # Si no quedan vecinos nuevos, retroceder
                camino.pop()

                if not camino:
                    print("\nTodos los cuadrantes accesibles han sido visitados.")
                    break

                anterior_x, anterior_y = camino[-1]

                if self.mover_robot(robot, vivienda, anterior_x, anterior_y):
                    print(f"Retrocediendo a ({anterior_x}, {anterior_y})")
                else:
                    print("No hay batería suficiente para retroceder.")
                    break