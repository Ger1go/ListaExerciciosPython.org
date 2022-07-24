#EXERCICIO 13..

#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

meses = ('1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio', '6 - Junho',
         '7 - Julho', '8 - Agosto', '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro')
temperaturas = {}

for mes in meses:
    temperaturas[mes] = float(
        input(f'Informe a temperatura media do mes de {mes} '))

somaTemperaturas = 0.0
for temperatura in temperaturas.values():
    somaTemperaturas += temperatura

mediaTemperaturaAnual = somaTemperaturas / 12.0

print(f'\n Temperaturas acima da media anual {mediaTemperaturaAnual:.2f}')
for mes in meses:
    if (temperaturas[mes] >= mediaTemperaturaAnual):
        print(f'\n {mes} - {temperaturas[mes]:.2f}')

