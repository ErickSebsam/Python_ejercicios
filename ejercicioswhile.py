import random
# 1. Leer una serie de números por parte del usuario hasta que el número ingresado sea negativo y determinar:
# *   Sumatoria de los números leídos
# *   Cantidad de números pares e impares
# *   El número menor y mayor leído


# n = 0
# pares = 0
# impares = 0
# total = 0
# mayor = 0
# menor = 0  

# while True:
#     n = int(input("Ingrese un numero: "))
    
#     if n < 0:
#         break

#     total = total + n
    
#     if n % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
        
#     if n > mayor:
#         mayor = n
#     if n < menor:
#         menor = n

# print(f"El total: {total}")
# print(f"Pares: {pares}")
# print(f"Impares: {impares}")
# print(f"Mayor: {mayor}")
# print(f"Menor: {menor}")



# 2. Leer un número y presentar la tabla de multiplicar de ese número entre 1 y 10.  Utilizar el siguiente formato de ejemplo:


# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5

# n = int(input("Ingrese un numero: "))
# for i in range(1,11): print(f"{n} x {i} = {n*i}")











# 3. En un partido de fútbol, se ofrece un descuento a los aficionados que depende del estrato y la edad.  
# Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la boleta.   
# Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%.  
# Si  el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y 
# Si el estrato es 2 y la edad es 18 años o más, el descuento será del 5%.  
# Determinar el total del dinero recaudado y descontado por las últimas N personas que ingresan al partido.



# N = int(input("Ingrese el numero de las últimas personas que ingresan al partido: "))
# total = 0
# descuento = 0
# descuentoT = 0
# a = 0
# while a < N:
#     estrato = int(input("Ingrese el estrato (1 o 2): "))
#     if estrato < 1 or estrato > 2:
#         print("¡Error! Solo se permite estrato 1 o 2. Intente de nuevo.")
#         continue
#     edad = int(input("Ingrese su edad: "))
#     valor = float(input("Ingrese el valor de la boleta: "))
#     descuento = 0
#     if estrato == 1 and edad < 18:
#         descuento = valor * 0.2
#         valor = valor - descuento
#     elif estrato == 1 and edad >= 18:
#         descuento = valor * 0.15
#         valor = valor - descuento
#     elif estrato == 2 and edad < 18:
#         descuento = valor * 0.1
#         valor = valor - descuento
#     elif estrato == 2 and edad >= 18:
#         descuento = valor * 0.05
#         valor = valor - descuento
#     a += 1
#     total= total+valor
#     descuentoT = descuentoT + descuento

# print(f"Total recaudado: ${total}")
# print(f"Total descontado: ${descuentoT}")





# 4. Realice un juego que simule el lanzamiento de un dado (muestre un valor aleatorio entre 1 y 6) 
# el programa debe llevar la cuenta del total de lanzamientos.  Si el jugador lanza 10 veces sin sacar 1 gana el juego, 
# en caso de sacar el 1 antes de los 10 lanzamientos pierde.
# Nota: si ya lanzó 10 veces sin sacar el 1 y ganó, no se le debe dejar volver a lanzar

# x = 1
# while x <= 10:
#     Inicio = input("Presione enter para lanzar el dado: ")
#     numero = random.randint(1, 6)
#     print(f"Lanzamiento: {x}")
#     print(f"numero: {numero}")
#     if numero == 1:
#         print("Perdió")
#         break
#     x+=1



# 5.  Leer un password de ingreso a un programa y mostrar el mensaje de bienvenida si es correcto. 
# Mientras no lo sea, debe mostrar el mensaje de Password incorrecto. 
# El programa debe terminar automáticamente al quinto intento fallido.

# password = "Hola Mundo"
# x = 1
# passwordN = ""
# while passwordN != password:
#     passwordN = input("Ingrese la contraseña: ")
#     if x < 5:
#         x+=1
#     else: 
#         print("Muchos intentos, semecuida")
#         break
#     if passwordN != password:
#         print("Contraseña incorrecta, intente otra vez :3")
#     else:
#         print("Contraseña correcta B)")
