# PREGUNTA 3

#Solicitando el numero de juguetes vendidos
payasos = int(input("Ingrese el numero de payasos vendidos: "))
munecas = int(input("Ingrese el numero de muñecas vendidas: "))

# Calculando el peso
peso_payaso = payasos * 112
peso_munecas = payasos * 75

# Mostrando los resultados
print(f"El Peso de los payasos es {peso_payaso} Kg, por su parte el Peso de las muñecas es {peso_munecas} Kg")
print("El Peso total es: ", peso_payaso + peso_munecas)