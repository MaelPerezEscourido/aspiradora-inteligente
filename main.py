from Modelo.vivienda import Vivienda
from Modelo.robot import Robot
from Control.controlador import Controlador
from Vista.vista import Vista


def main():

    # Crear vivienda
    vivienda = Vivienda()
    vivienda.agregar_zona("Salon", 2, 2)

    # Asignar suciedad
    vivienda.obtener_cuadrante("Salon", 0, 0).establecer_suciedad(70)
    vivienda.obtener_cuadrante("Salon", 1, 0).establecer_suciedad(30)
    vivienda.obtener_cuadrante("Salon", 0, 1).establecer_suciedad(90)

    # Colocar un obstáculo en el cuadrante (1, 0)
    vivienda.establecer_obstaculo("Salon", 1, 0)

    # Crear robot
    robot = Robot(bateria=80)
    robot.actualizar_posicion("Salon", 0, 0)

    # Crear controlador y vista
    controlador = Controlador()
    vista = Vista()

    # Estado inicial
    print("\nANTES DE LIMPIAR")
    vista.mostrar_estado_robot(robot)
    vista.mostrar_vivienda(vivienda)

    # Limpiar toda la zona automáticamente
    print("\nINICIANDO LIMPIEZA AUTOMÁTICA")
    controlador.limpiar_zona(robot, vivienda)

    # Estado final
    print("\nDESPUÉS DE LIMPIAR")
    vista.mostrar_estado_robot(robot)
    vista.mostrar_vivienda(vivienda)


if __name__ == "__main__":
    main()