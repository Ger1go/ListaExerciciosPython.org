#EXERCICIO 17.. Faça um Programa para uma loja de tintas.

#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 80,00 ou em galões de 3.6 litros, que custam 25,00.

#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;

#comprar apenas galões de 3,6 litros;

#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print('Olá mundo! Vamos calcular quantas latas de pintura precisa para pintar a suas paredes? \n')
m2 = int(input('Quantos m2 precisa pintar?: '))
print('\n')


import math
litro = (m2 / 6) * 1.1
latas = math.ceil(litro / 18)
preço_lata = float(latas * 80)
galao = math.ceil(litro / 3.6)
preço_galao = float(galao * 25)



print(f'Se você compra apenas latas de 18L vai precisar um total de {latas} lata(s) que custa R$80 cada, contabilizando um total de R${preço_lata} . \n')
print(f'Se você compra apenas galões de 3.6L vai precisar um total de {galao} galão(ões) que custam R$25 cada, contabilizando um total de R${preço_galao} . \n')
print(f'Se você compra galôes de 3.6L mais latas de 18L, acrescentando 10% a mais de folga e procurando o menor custo possivel, vai precisar de: ')

mixlatas = round(litro / 18)
mixgaloes = round((litro - mixlatas * 18) / 3.6)



if litro - (mixlatas * 18) % 3.6 != 0:
  mixgaloes = mixgaloes + 1
  totalmix = (mixlatas * 80) + (mixgaloes * 25)


print(f'{mixlatas} lata(s) '
      f'e {mixgaloes} galão(ões), somando um total de: R${totalmix:.2f}.\n')