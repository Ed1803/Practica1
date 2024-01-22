#PREGUNTA 11
# Lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
print("Lista con elementos duplicados:",lista_original)
# Convertir la lista a un conjunto (set) 
conjunto = set(lista_original)
lista_final= list(conjunto)
print("Lista sin elementos duplicados:", lista_final)