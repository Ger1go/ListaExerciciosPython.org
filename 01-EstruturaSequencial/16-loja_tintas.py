#EXERCICIO 16 .. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print('Olá mundo! Vamos calcular quantas latas de pintura precisa para pintar a suas paredes? \n')
m2 = int(input('Quantos m2 precisa pintar?: '))

litro = m2 * 3 / 1
latas = int(litro / 18)
preço = float(latas * 80)

print(f'Você precisa {latas} latas que custam R$80 cada, contabilizando um total de R${preço} .')

