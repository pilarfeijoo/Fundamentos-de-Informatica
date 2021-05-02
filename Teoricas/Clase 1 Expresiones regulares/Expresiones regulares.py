print("asdsads\ndasdas")
print("asdsads\t\t\tdasdas")

import re
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
#si lo encuentra(hace match) nos devuelve la ubicacion
print(re.search("amet", texto))
# <re.Match object; span=(22, 26), match='amet'>

#El función match() de re busca el patrón y devuelve la primera aparición y solo al principio de la cadena. Si se encuentra una coincidencia
#  en la primera línea, devuelve el objeto de coincidencia. Pero, si se encuentra una coincidencia en alguna otra línea, devulve un valor nulo.
print(re.match("amet", texto))
# NONE  

#Group me devuelve el string puro
print(re.search("amet", texto).group(0))
#amet


#Todas las ocurrencias dentro de una lista
print(re.findall("amet", texto))
# [`amet', 'amet']


#X(.*)Y
#Lo que esta entre X e Y
# El punto (.) para indicar que puede ser cualquier carácter, y el asterísco (*) para indicar que puede haber 0 o más de estos caracteres


print(re.search("ipsum(.*)sit", texto).group())
#Lorem (ipsum dolor sit amet, consectetur ipsum elit. Amet sit) amet.
print()

print(re.search("ipsum(.*)sit", texto).group(1))
#Lorem ipsum (dolor sit amet, consectetur ipsum elit. Amet) sit amet.


# Existe una forma de priorizar los matches internos y es con el metacarácter ?:

print()
print(re.search("ipsum(.*?)sit", texto).group(0))
#Lorem (ipsum dolor sit) amet, consectetur ipsum elit. Amet sit amet.

print(re.findall("ipsum(.*?)sit", texto))

print()
print(re.sub("Amet", "BOKITA", texto))

#Colocando r antes interpretara \n literalmente y no como un salto del linea
print(r"\n")

if re.search("Amet", texto) is not None:
	print("Busqueda Afirmativa")


#Union de rangos
# [a-zA-z1-9]

#Con las expresiones regulares se puede utilizar un metacarácter \b el cual delimita caracteres alfanúmericos de otros que no lo son.
#De esta manera podemos obtener las palabras de alguna frase si delimitamos la búsqueda con este metacarácter al inicio y al final.
#Así podemos, por ejemplo, reemplazar fácilmente alguna palabra en particular.

#patron = r"\bipsum\b"

#bONUS

# (\W|^) Indico que antes de la palabra puede haber alguno caracter no alfanumerico como un espacio o que este en el inicio de la linea
#(?i) hace que la concordancia de contenido no distinga entre mayúsculas y minúsculas.
#El punto «.» es el comodín, representa cualquier carácter excepto el salto de línea. De este modo: