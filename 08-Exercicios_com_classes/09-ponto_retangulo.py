#EXERCICIO 9...

#-Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

#-Possua uma classe chamada Ponto, com os atributos x e y.

#-Possua uma classe chamada Retangulo, com os atributos largura e altura.

#-Possua uma função para imprimir os valores da classe Ponto

#-Possua uma função para encontrar o centro de um Retângulo.

#-Você deve criar alguns objetos da classe Retangulo.

#-Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.

#-A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

#-O valor do centro do objeto deve ser mostrado na tela Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.


class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimeValores(self):
        print(f'X: {self.x}, Y: {self.y}')

class Retangulo:

    def __init__(self, altura, largura, centro):
        self.altura = altura
        self.largura = largura
        self.centro = centro

    def mostraCentro(self):
        self.centro.imprimeValores()

ponto1 = Ponto(10, 20)
ponto2 = Ponto(30, 40)

ret1 = Retangulo(10, 20, ponto1)
ret2 = Retangulo(30, 40, ponto2)
ret1.mostraCentro()
ret2.mostraCentro()