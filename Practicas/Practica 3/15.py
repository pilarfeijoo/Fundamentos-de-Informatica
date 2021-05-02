#15.Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
mail = "marturoch@ucema.com"
patron = "(\W|^)[^(()<>@,;:%]*(@)((yahoo|hotmail|gmail).com)(\W|$)" #lo hice con .com
if re.search(patron, mail) is not None:
    print("Su mail es valido")
else:
    print("su mail es invalido")
#PREGUNTAR, no sabemos bien que esta permitido en los mails. Lo que esta desp del @, como lo sabemos si hay miles de opciones.

# (\W|^) Indico que antes de la palabra puede haber alguno caracter no alfanumerico como un espacio o que este en el inicio de la linea
\