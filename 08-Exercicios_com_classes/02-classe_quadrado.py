#EXERCICIO 2...

#Classe Quadrado: Crie uma classe que modele um quadrado:

#Atributos: Tamanho do lado

#Métodos: Calcular Área

class Quadrado:
  def __init__(self, lado = 1):
    self.lado = lado

  def calcular_area(self):
    return self.lado ** 2

quadrado = Quadrado(6)
print(quadrado.lado, quadrado.calcular_area())

