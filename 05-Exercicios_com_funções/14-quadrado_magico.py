#EXERCICIO 14...

#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, #veja um quadrado mágico de lado 3, com números de 1 a 9:

#  8  3  4 
#  1  5  9
#  6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

print("***** Quadrados magicos *****")

algarismos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
combinacoes_15 = []
def valida_linha(lista):
    for i in lista:
        for j in lista:
            for h in lista:
                if  i + j + h == 15 and (i != j and i != h and j != h):
                    combinacoes_15.append([i, j, h])
    return combinacoes_15

def monta_quadrado(combinacoes):
    linha2 = []
    linhas = []
    quadrado_perfeito = []
    for i in combinacoes:
        if i[0] % 2 != 0 and i[1] == 5 and i[2] % 2 != 0 :
            linha2.append(i)
    for i in combinacoes:
        if i[0] % 2 == 0 and i[1] % 2 != 0 and i[1] != 5 and i[2] % 2 == 0:
            linhas.append(i)
    for l2 in linha2:
        for linha1 in linhas:
            for linha3 in linhas:
                if l2[0] + linha1[0] + linha3[0] == 15 and l2[2] + linha1 [2] + linha3[2] == 15:
                    quadrado_perfeito.append([linha1, l2, linha3])
    for i in quadrado_perfeito:
        print(f'       {i[0]}')
        print(f'       {i[1]}')
        print(f'       {i[2]}')
        print('       ' + '-'* 9)


valida_linha(algarismos)
monta_quadrado(combinacoes_15)

