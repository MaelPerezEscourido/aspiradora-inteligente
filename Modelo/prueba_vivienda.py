
from Modelo.vivienda import Vivienda

# Creamos la vivienda
casa = Vivienda()

# Creamos las zonas
casa.agregar_zona("Salon", 3, 3)
casa.agregar_zona("Cocina", 3, 3)
casa.agregar_zona("Dormitorio", 3, 3)

# Asignamos suciedad a algunos cuadrantes
casa.obtener_cuadrante("Salon", 0, 0).suciedad = 80
casa.obtener_cuadrante("Salon", 1, 0).suciedad = 90

casa.obtener_cuadrante("Cocina", 0, 0).suciedad = 40
casa.obtener_cuadrante("Dormitorio", 0, 0).suciedad = 60

# Mostramos el estado de la vivienda
casa.mostrar_vivienda()

# Comprobamos el porcentaje de suciedad de cada zona
print("\n--- ESTADO DE LAS ZONAS ---")

for zona in casa.zonas.values():
    print(
        f"{zona.nombre}: "
        f"{zona.calcular_suciedad():.2f}% de suciedad"
    )
    print(
        "¿Está limpia?",
        zona.esta_limpia()
    )
