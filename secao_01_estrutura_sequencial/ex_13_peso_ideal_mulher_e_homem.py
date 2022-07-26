#EXERCICIO 13.. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#a- Para homens: (72.7*h) - 58
#b- Para mulheres: (62.1*h) - 44.7

sex = input('Por favor, digite a sua altura para calcular seu peso ideal. \nMas primeiro informe seu sexo, digite "h"para homem e "m" para mulher:  ')
alt = float(input('Agora por favor, digite a sua altura: '))
if sex == 'h':
    peso1 = 72.7*alt - 58
    inteiro = int(peso1)
    print(f"O seu peso ideal é: {inteiro}Kg")
else:
    peso2 = 62.1*alt - 44.7
    inteiro = int(peso2)
    print(f'O seu peso ideal é: {inteiro}kg')