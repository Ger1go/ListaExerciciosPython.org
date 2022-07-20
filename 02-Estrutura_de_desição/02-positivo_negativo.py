#EXERCICIO 2...Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Informe um numero: '))

if (num > 0):
    print(num, 'é positivo')
elif (num < 0):
    print(num, 'é negativo')
else:
    print('O numero é igual a 0')