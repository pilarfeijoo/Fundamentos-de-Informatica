from aves import *

class EntrenadorDeDragones():
   def __init__(self, vacantes):
      self.vacantes = vacantes
      self.dragones_aceptados = []

    def aceptar_dragones(self, ave):
        if self.vacantes - 1 > 0:
          self.dragones_aceptados.append(ave)
          self.vacantes -= 1

    def entrenador_dragones(self):
      for dragon in self.dragones_aceptados:
        for i in range(0,20):
            dragon.volar_en_circulos()

        dragon.comer_peces(3) 