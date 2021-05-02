#bajando el requerimiento a detalle:
#- crear la clase "EntrenadorDeDragones"
 #-por que? Porque:
 # -Todo objeto tiene que ser instancia de una clase
  #-Porque podriamos tener mas de una instancia de EntrenadorDeDragones (es decir, tener mas entrenadores)
#-crear a 'hipo', que es un "EntrenadorDeDragones"
#-La clase "EntrenadorDeDragones" tiene que:
# -Definir un metodo   
 #-Definir un metodo

cuando tenemps dos o mas objetos que comparten una interfaz 

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia = self.energia + 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia <= 10

class Dragon:
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def saciar(self)
    self.comer_peces(3)

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 1000)