#EXERCICIO 3...

#Classe Retangulo: Crie uma classe que modele um retangulo:

#A- Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

#B- Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

#C-Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:

    def __init__(self, base, altura):
        self.setBase(base)
        self.setAltura(altura)

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def setAltura(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura

    def calculaArea(self):
        return self.base * self.altura

    def calculaPerimetro(self):
        return 2 * self.base + 2 * self.altura

# TESTE DA CLASSE
base = int(input('Informe o valor da base: '))
altura = int(input('Informe o valor da altura: '))
retangulo = Retangulo(base, altura)
print(f'A area do retangulo é: {retangulo.calculaArea()}') 
print(f'O perimetro do retangulo é: {retangulo.calculaPerimetro()}')
