#EXERCICIO 4...

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def arg(b):
    if b > 0:
      return  'P'
    else:
      return  'N'

b = int(input('Digite um valor positivo ou negativo: '))

print('Seu valor corresponde com um argumento do tipo: ', arg(b))
