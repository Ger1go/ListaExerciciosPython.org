#EXERCICIO 8 ..

#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

#Se a gente arredondar o número para baixo, e depois somar 1, o resultado sempre vai dar a quantidade de digitos. No caso decidi definir como inteiro e depois somar 1. 

def quantidade_digitos(numero):
    import math
    return int(math.log(numero, 10) +1)
#Utilizo a função abs(), ou seja, valor absoluto do número, caso o usuario decida utilizar um número inteiro negativo. 

numero = abs(int(input('Digite um número inteiro: ')))
quantidade_digitos(numero)

print(f'O número {numero} tem {quantidade_digitos(numero)} digitos. ')
