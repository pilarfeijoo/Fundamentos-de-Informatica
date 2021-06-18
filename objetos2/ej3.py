#ejercicio 3

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer(self, gramos): 
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
    return self.energia <= 10

  def saciar(self):
    self.comer_alpiste(100)

  def esta_en_equilibrio(self):
    return self.energia > 150 and self.energia < 300 

class Gorrion:
    def __init__(self, kms, gramos):
        self.kms = kms
        self.gramos = gramos
        self.comidas = []
        self.vuelos = []
    def volar(self, longitud):
        if longitud > 0:
            self.vuelos.append(longitud)
            self.kms += longitud   
    def comer(self, ingerido):
        if ingerido > 0:
            self.comidas.append(ingerido)
            self.gramos += ingerido   
    def CSS(self):
        if self.gramos <= 0:
            return "no puedo devolver el CSS, porque no ha ingerido comida"
        else:
            return self.kms / self.gramos
    def CSSP(self):
        if self.gramos <= 0:
            return "no puedo devolver el CSSP, porque no ha ingerido comida"
        else:
            return int(max(self.vuelos)) / int(max(self.comidas))
    def CSSV(self):
        if len(self.comidas) <= 0:
            return "no puedo devolver el CSSV, porque no ha hingerido comida"
        else:
            return int(len(self.vuelos)/len(self.comidas))
    def esta_en_equilibrio(self): 
        return self.gramos > 100 and self.gramos < 300 

class Ornitologo:
    def __init__(self):
        self.aves = []
    def estudiarAve(self, ave):
        self.aves.append(ave)
    def avesEnEstudio():
        return self.aves
    def realizarRutinaSobreAves(self):
        for ave in self.aves:
            ave.comer(80)
            ave.volar(70)
            ave.comer(10)
    def avesEnEquilibrio(self,ave):
        return ave.esta_en_equilibrio()