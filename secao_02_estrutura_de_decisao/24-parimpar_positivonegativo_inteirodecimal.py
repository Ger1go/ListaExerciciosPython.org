#EXERCICIO 24..

#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#par ou ímpar;

#positivo ou negativo;

#inteiro ou decimal.

num1 = int(input('Digite o primeiro numero: \n'))
num2 = int(input('Digite o segundo numero: \n'))

op = int(input('Escolha um tipo de operação: \n *- Digite 1 para soma: \n *- Digite 2 para resta: \n *- Digite 3 para divisão: \n *- Digite 4 para multiplicação: \n '))

if op > 4:
  print('Opção invalida!')
  
else:
 if op == 1:
    res = num1 + num2
    print(f'Você escolheu uma soma, o resultado de {num1} + {num2} é: {res}. \n')
 elif op == 2:
    res = num1 - num2
    print(f'Você escolheu uma resta, o resultado de {num1} - {num2} é: {res}. \n')
 elif op == 3:
    res = num1 / num2
    print(f'Você escolheu uma divisão, o resultado de {num1} / {num2} é: {res}. \n')
 elif op == 4:
    res = num1 * num2 
    print(f'Você escolheu uma multiplicação, o resultado de {num1} X {num2} é: {res}. \n')

 if res % 2 == 1:
    print('O resultado da sua opereção deu um numero IMPAR. \n')
 else:
    print('O resultado da sua opereção deu um numero PAR. \n')

 if res < 0:
    print('Alias, o resultado da sua opereção deu um numero NEGATIVO. \n' )
 else:
    print('Alias, o resultado da sua opereção deu um numero POSITIVO. \n' )
 if res % 1 == 0:
  print('Finalmente, seu numero também tem a carateristica de ser um INTEIRO!.')
 else:
    print('Finalmente, seu numero também tem a carateristica de ser um DECIMAL!.')

    