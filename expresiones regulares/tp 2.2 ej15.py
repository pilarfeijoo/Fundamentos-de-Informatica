#15 Realizá un programa que validar si una cuenta de mail está escrita correctamente.

import re
mail = "feijoopilar@gmail.com"
patron = "[^(()<>@,;:%]*(@)(gmail.com{1})" 
if re.search(patron, mail) is not None:
    print("Su mail es valido")
else:
    print("su mail es invalido")