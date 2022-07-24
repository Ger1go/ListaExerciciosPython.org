#EXERCICIO 6...

#Classe TV: Faça um programa que simule um televisor criando-o como um objeto.

#O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.

#Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV:

    def __init__(self):
        self.volume = 0
        self.setCanal(0)

    def setCanal(self, canal):
        if (canal >= 0) and (canal <= 100):
            self.canal = canal

    def aumentaVolume(self):
        if (self.volume < 100):
            self.volume += 1

    def diminuiVolume(self):
        if (self.volume > 0):
            self.volume -= 1

# TESTE DA CLASSE
tv = TV()
tv.setCanal(10)
tv.aumentaVolume()
tv.aumentaVolume()
tv.aumentaVolume()
tv.aumentaVolume()
tv.diminuiVolume()
print(f'Canal: {tv.canal} - Volume: {tv.volume}')
