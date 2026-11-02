from Modelo.robot import Robot

# Creamos el robot
robot = Robot()

# Mostramos su batería inicial
print("Batería inicial:", robot.obtener_bateria(), "%")

# Actualizamos su posición
robot.actualizar_posicion("Salon", 1, 2)

print("Zona actual:", robot.zona_actual)
print("Posición:", robot.x, robot.y)

# Simulamos un consumo de batería
robot.consumir_bateria(25)

print("Batería después del consumo:", robot.obtener_bateria(), "%")

# Comprobamos que la batería no baja de cero
robot.consumir_bateria(100)

print("Batería final:", robot.obtener_bateria(), "%")