Ejercicio 2
#Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

TODO: PARARSE EN PRACTICA 6 PARA QUE FUNCIONE

class Golondrina:
  def __init__(self, energia): 
                                    
  def comer_alpiste(self, gramos):  
    self.energia += 4 * gramos     

  def volar_en_circulos(self): 
    self.volar(0)

  def volar(self, kms):
    if self.energia > 10 + kms:
      self.energia -= 10 + kms
    else:
      print("No tengo energia suficiente, necesito comer alpiste")


pepita = Golondrina(42)   

# >>> from ej2 import Golondrina, pepita
# >>> pepita.energia
# 42  
# >>> pepita.volar(20)  
# >>> pepita.energia
# 12  
# >>> pepita.volar(30) 
# No tengo energia suficiente, necesito comer alpiste
