#3 Creá un programa que verifique las siguientes condiciones:

# si un string dado tiene una h seguida de ninguna o más e.
# si un string dado tiene una h seguida de una o más e.
# si un string dado tiene una h seguida de una o más e.
# si un string dado tiene una h seguida de dos o tres e. 

import re

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

    print(encontrar_patron("a"))
    print(encontrar_patron("h"))
    print(encontrar_patron("he"))
    print(encontrar_patron("heeeeee"))
    