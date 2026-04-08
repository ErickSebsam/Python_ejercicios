productos_producidos= int(input("Ingrese el numero de productos producidos: "))
productos_recolectados= int(input("Ingrese la cantidad de productos recolectados: "))
indice_de_cosecha= productos_recolectados/productos_producidos
print(f"El indice de cosecha es de {indice_de_cosecha*100}%")