#EXERCICIO 22..

#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:

#necessita da esfera;
#necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
#  Quantidade de mouses: 100

#  Situação                        Quantidade              Percentual
#  1- necessita da esfera                  40                     40%
#  2- necessita de limpeza                 30                     30%
#  3- necessita troca do cabo ou conector  15                     15%
#  4- quebrado ou inutilizado              15                     15%

idMouse = -1
defeitos = ('1 - Necessita de Esfera',
            '2 - Necessita de limpeza',
            '3 - Necessita troca de cabo ou conector',
            '4 - Quebrado ou inutilizado')


totalDefeitos = [0] * 4
totalMouses = 0

for i in defeitos:
    print(f'{i}')

print('\n')

while (idMouse != 0):
    idMouse = int(input('Identificador do Mouse: '))
    if (idMouse != 0):
        defeito = int(input('Codigo do defeito: '))
        totalDefeitos[defeito - 1] += 1
        totalMouses += 1

print(f'\nQuantidade de mouses: {totalMouses} ')

print('\nSituacao\t\t\t\tQuantidade\t\t   Percentual')


for i in range(4):
    if i == 2:
      print(f'{defeitos[i]} \t {totalDefeitos[i]}\t\t\t{totalDefeitos[i]/float(totalMouses) * 100:.1f}%' )
    else:
      print(f'{defeitos[i]} \t\t\t {totalDefeitos[i]}\t\t\t{totalDefeitos[i]/float(totalMouses) * 100:.1f}%' )

      