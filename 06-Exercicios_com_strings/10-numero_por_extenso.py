#EXERCICIO 10...

#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

dezenas = ['', '', 'vinte', 'trinta', 'quarenta',
           'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
primeira_dezena = ['dez', 'onze', 'doze', 'treze', 'catorze',
                   'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
unidades = ['zero', 'um', 'dois', 'tres', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove']

numero = int(input('Informe um numero: '))
if (numero < 0) or (numero > 99):
    print('O numero informado deve estar entre 0 e 99')
else:
    dezena = int(numero / 10)
    unidade = int(numero % 10)
    print('O numero por extenso é:', end = ' ')


    if (numero >= 20):
        print(f'{dezenas[dezena]}', end = ' ')
        if (unidade != 0):
            print(f'e {unidades[unidade]}')
        print
    elif (numero >= 10):
        print(f'{primeira_dezena[unidade]}') 
    else:
        print(f'{unidades[unidade]}')

