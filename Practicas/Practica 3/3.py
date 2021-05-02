#3. Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de dos o tres e.
import re 
string = input("Ingrese un string:")
patron1 = "(h(e*))"
patron2 = "(h(e+))"
patron3 = "(h(e{2,3})[^e])"

if re.search(patron1, string) is not None:
    print("El string tiene una h seguida de ninguna o mas e")
else:
    print("El string no tiene una h seguida de ninguna o mas e")

if re.search(patron2, string) is not None:
    print("El string tiene una h seguida de una o mas e")
else:
    print("El string no tiene una h seguida de una o mas e")

if re.search(patron3, string) is not None:
    print("El string tiene una h seguida de dos o tres e")
else:
    print("El string no tiene una h seguida de dos o tres e")