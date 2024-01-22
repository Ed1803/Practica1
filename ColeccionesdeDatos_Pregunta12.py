#PREGUNTA 12

nombre_archi = input("Ingrese el nombre del archivo: ")
nombre, formato = nombre_archi.split(".")

tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

# En caso de encontrarse formato en tipos_mine devolvera eso, pero de caso contrario se colocara lo segundo por defecto
tipo_mime = tipos_mime.get(formato, 'application/octet-stream')

# Mostrar el resultado
print(f"Tipo MIME: {tipo_mime}")