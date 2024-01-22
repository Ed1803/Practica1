# PREGUNTA 8

hora = input("Ingrese la hora en formato de 24 horas (HH:MM): ")

horas, min = hora.split(":")
horas = int(horas)
min = int(min)

hora_final = horas + min / 60

if 7.0 <= hora_final <= 8.0:
    print("Es hora de desayunar.")
elif 12.0 <= hora_final <= 13.0:
    print("Es hora de almorzar.")
elif 18.0 <= hora_final <= 19.0:
    print("Es hora de cenar.")
else:
    pass
