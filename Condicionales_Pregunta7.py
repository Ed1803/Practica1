# PREGUNTA 7

num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))

print("1. Suma de los dos números")
print("2. Resta (primer número menos segundo número)")
print("3. Multiplicación de los dos números")

# Leer la opción del usuario
opcion = input("Seleccione una opción: ")

# Realizar operación según la opción seleccionada
if opcion == '1':
      resultado = num_1 + num_2
      print(f"La suma de {num_1} y {num_2} es: {resultado}")
elif opcion == '2':
      resultado = num_1 - num_2
      print(f"La resta de {num_1} menos {num_2} es: {resultado}")
elif opcion == '3':
      resultado = num_1 * num_2
      print(f"La multiplicación de {num_1} y {num_2} es: {resultado}")
else:
      print("ERROR, INGRESE NUEVAMENTE")
      