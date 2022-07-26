#EXERCICIO 8 ...

#Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().

#Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.

#Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        print('Bucho:', self.bucho)

    def digerir(self):
        if (len(self.bucho) > 0):
            self.bucho.pop(0)

# Teste
macaco1 = Macaco('Simao')
macaco2 = Macaco('Prego')

macaco1.comer('Maca')
macaco1.verBucho()
macaco1.comer('Banana')
macaco1.verBucho()
macaco1.comer('Abacaxi')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()
macaco2.comer('Maca')
macaco2.comer('Banaca')
macaco2.comer(macaco1.nome)
macaco2.verBucho()
