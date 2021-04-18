#1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

import re

texto = "Pilar2"
patron = "[a-zA-Z0-9]"

if re.search(patron, texto) is not None:
    print("Algun elemento de este rango se encuentra en el string")


