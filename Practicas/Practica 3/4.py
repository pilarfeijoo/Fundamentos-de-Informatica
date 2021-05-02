#4. Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re 
string = "Hola mi nick es Mr_Portnoy jeje"
patron = "(\w*)_(\w*)"
print(re.search(patron, string).group(0))
