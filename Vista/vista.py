class Vista:

    def mostrar_estado_robot(self, robot):
        print("\n========== ESTADO DEL ROBOT ==========")
        print(f"Zona actual: {robot.zona_actual}")
        print(f"Posición: ({robot.x}, {robot.y})")
        print(f"Batería: {robot.bateria}%")
        print(f"Velocidad: {robot.velocidad:.2f}%")

    def mostrar_vivienda(self, vivienda):
        print("\n========== ESTADO DE LA VIVIENDA ==========")
        vivienda.mostrar_vivienda()