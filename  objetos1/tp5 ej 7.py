Ejercicio 7
#Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorrion:
    def __init__(self, kms, gramos):
        self.comidas = []
        self.vuelos = []
        self.kms = kms
        self.gramos = gramos

    def volar(self, longitud):
        self.vuelos.append(longitud)
        self.kms += longitud
    
    def comer(self, ingerido):
        self.comidas.append(ingerido)
        self.gramos += ingerido
    
    def CSS(self):
        return self.kms/self.gramos
    
    def CSSP(self):
        if self.gramos <= 0:
            return None
        else:
            return (int(max(self.vuelos)) / int(max(self.comidas)))
    
    def CSSV(self):
        return (int(max(self.vuelos)) / int(max(self.comidas)))


pedro = Gorrion(0,0)
pedro.comer(100)
pedro.comer(200)
pedro.comer(300)
pedro.volar(10)
pedro.volar(20)
pedro.volar(30)


    