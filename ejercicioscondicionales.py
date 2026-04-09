#
#
# En un sistema de automatización industrial, un motor puede estar encendido o apagado.
# Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente.
# Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.


# estado_motor = input("Ingrese el estado del motor (encendido o apagado): ")
# temperatura = int(input("Ingrese la temperatura del motor en grados: "))

# if estado_motor == "encendido" and temperatura > 80:
#     estado_motor ="pagado"
#     print("Temperatura excesiva, apagado")
#     print("Estado del motor:", estado_motor)
# else:
#     print("Temperatura correcta, maquina encendida")
#     print("Estado del motor:", estado_motor)


# Un programa de descarga de archivos multimedia tiene diferentes velocidades de descarga según la calidad de la conexión a internet del usuario.
# Si la conexión es mayor a 20 Mbps, la velocidad de descarga será de 10 Mbps, si la conexión es menor a 20 Mbps pero mayor a 5 Mbps, la velocidad será
# de 5 Mbps y si la conexión es menor a 5 Mbps,
# la velocidad de descarga será de 1 Mbps. Escribir un programa que calcule el tiempo de descarga de un archivo y el ancho de banda utilizado, según
# la velocidad de descarga.


# calidad_conexion = float(input("Ingrese la calidad de la conexión en Mbps: "))
# velocidad_descarga = 0
# archivo = float(input("Ingrese el tamaño del archivo en Mb: "))

# if calidad_conexion > 20:
#     velocidad_descarga = 10
# elif calidad_conexion > 5 and calidad_conexion <= 20:
#     velocidad_descarga = 5
# else:
#     velocidad_descarga = 1

# tiempo_descarga = archivo/velocidad_descarga
# print(f"Velocidad de descarga: {velocidad_descarga}Mbps")
# print(f"El tiempo de descarga es de {tiempo_descarga} segundos")
# print(f"El ancho de banda utilizado es de {calidad_conexion} Mbps")

# 3.  Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad.
# Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la matrícula.
# Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%.
# Si el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y
# si el estrato es 2 y la edad es 18 años o mas, el descuento será del 5%.
# Escribir el precio que deberá pagar un estudiante por su matrícula y el valor del descuento.

# estrato = input("Por favor digite el estrato (entre 1 y 2): ")
# edad = int(input("Por favor digite su edad: "))
# matricula = float(input("Por favor digite el valor de la matricula: "))
# descuento = 0
# if estrato == "1" and edad < 18:
#     print("El descuento es del 20%")
#     descuento = matricula*0.2
#     matricula = matricula-descuento
#     print(f"El nuevo valor de la matrícula es de {matricula}")
#     print(f"El valor descontado es de {descuento}")
# elif estrato == "1" and edad >= 18:
#     print("El descuento es del 15%")
#     descuento = matricula*0.15
#     matricula = matricula-descuento
#     print(f"El nuevo valor de la matrícula es de {matricula}")
#     print(f"El valor descontado es de {descuento}")
# elif estrato == "2" and edad < 18:
#     print("El descuento es del 15%")
#     descuento = matricula*0.1
#     matricula = matricula-descuento
#     print(f"El nuevo valor de la matrícula es de {matricula}")
#     print(f"El valor descontado es de {descuento}")
# else:
#     print("El descuento es del 5%")
#     descuento = matricula*0.05
#     matricula = matricula-descuento
#     print(f"El nuevo valor de la matrícula es de {matricula}")
#     print(f"El valor descontado es de {descuento}")


# 4.  Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
# un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo.

# Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde,
# se determina su resultado como positivo y en caso contrario como negativo.

#   La tabla en la que el medico se basa para obtener el resultado es la siguiente:

# nivel_hemoglobina = float(input("Ingrese su nivel de hemoglobina en la sangre (g%): "))
# edad_meses = int(input("Ingrese su edad en meses :3: "))
# edad_ano = edad_meses / 12
# sexo = input("Ingrese su sexo (f/m): ")

# if edad_meses <= 1 and 13 >= nivel_hemoglobina <= 26:
#     print("El paciente no tiene anemia")
# elif edad_meses > 1 and edad_meses <= 6 and 10 <= nivel_hemoglobina <= 18:
#     print("El paciente no tiene anemia")
# elif edad_meses > 6 and edad_meses <= 12 and 11 <= nivel_hemoglobina <= 15:
#     print("El paciente no tiene anemia")
# elif edad_ano > 1 and edad_ano <= 5 and 11.5 <= nivel_hemoglobina <= 15:
#     print("El paciente no tiene anemia")
# elif edad_ano > 5 and edad_ano <= 10 and 12.6 <= nivel_hemoglobina <= 15.5:
#     print("El paciente no tiene anemia")
# elif edad_ano > 10 and edad_ano <= 15 and 13 <= nivel_hemoglobina <= 15.5:
#     print("El paciente no tiene anemia")
# elif edad_ano > 15 and sexo == "f" and 12 <= nivel_hemoglobina <= 16:
#     print("El paciente no tiene anemia")
# elif edad_ano > 15 and sexo == "m" and 13 <= nivel_hemoglobina <= 18:
#     print("El paciente no tiene anemia")
# else:
#     print("El paciente tiene anemia")


# En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para determinar si cumplen con los estándares de calidad.
# Si la pieza es defectuosa, se debe marcar como rechazada y enviar una alerta al operador.
# Si la pieza cumple con los estándares de calidad, se debe marcar como aprobada y continuar con la producción.
# Realice un programa que lea una entrada binaria en la que los 1s significan estándares de calidad cumplidos y los 0s significan estándares de
# calidad No cumplidos.
# El programa debe rechazar la pieza ante cualquier estándar no cumplido.


calidad = input("Ingrese el estandar de calidad (1-cumplido/0-no cumplido)")
estado = ""
if calidad == "1":
    estado = "No defectuosa"
    print("La pieza ta buena")
    print(f"Estado: {estado}")
else: 
    estado = "Defectuosa"
    print("La pieza no ta buena")
    print(f"Estado: {estado}")
