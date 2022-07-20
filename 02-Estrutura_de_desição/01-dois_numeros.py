#EXERCICIO 1..Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))

if (num1 > num2):
    print(num1, 'eh maior que', num2)
elif (num1 < num2):
    print(num2, 'eh maior que', num1)
else:
    print('Os numeros sao iguais')