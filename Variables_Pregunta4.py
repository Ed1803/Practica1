# PREGUNTA 4

#Ingresando el entero positivo
numero = int(input("Ingrese un numero entero positivo: "))
if numero > 0:
  sumatoria = numero * (numero + 1)/2
  print(f"La Sumatoria de los {numero} primeros numeros es {sumatoria}")
else:
  if numero == 0:
    print("La Sumatoria es 0")
  else:
    print("ERROR AL INGRESAR EL NUMERO POSITIVO")