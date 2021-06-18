#ejercicio4
class MedioDeTransporte:
    def __init__(self,combustible_en_litros):
        self.combustible_en_litros = combustible_en_litros
        self.personas = []
    def cargar_combustible(self,litros):
        self.combustible_en_litros += litros
    def agregar_pasajeros(self,cantidad_pasajeros):
        if cantidad_pasajeros <= 5 - len(self.personas):
            for _ in range(cantidad_pasajeros):
                self.personas.append(cantidad_pasajeros)
        else:
            return "No puedo agregar mas pasajeros"
class Moto(MedioDeTransporte):
    def recorrer_distancia(self, distancia_en_kms):
        self.combustible_en_litros -= distancia_en_kms * 0,5
class Auto(MedioDeTransporte):
    def recorrer_distancia(self, distancia_en_kms):
        self.combustible_en_litros -= distancia_en_kms
        