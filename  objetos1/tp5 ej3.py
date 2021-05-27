Ejercicio 3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

lass Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio       
        
    def descuento(self, numero):
        self.precio *= 1 - numero/100

from ej3 import Notebook, mac
mac = Notebook('apple', 'air', 1000)

# >>> from ej3 import Notebook, mac
# >>> mac
# <ej3.Notebook object at 0x7f93a82cefd0>
# >>> mac.marca
# 'apple'
# >>> mac.modelo
# 'air'
# >>> mac.precio
# 1000
# >>> mac.descuento(50)
# >>> mac.precio
# 500.0