#EXERCICIO 20.. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

#------------------------------
#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
#mudar 1==0 por 1==1 para ativar o exercicio 

#------------------------------


while 1==0: 
  fat = int(input('Digite um numero inteiro para calcular a sua expressão fatorial: '))

  while fat>16 or fat<0:
    fat=int(input("numero incorreto,informe outro numero-->"))
  else: 
    
    cont = fat
    f = 1

    print(f'Calculando {fat}! = ', end = '')
    while cont > 0:
      print(f'{cont}', end = '')
      print(f' x ' if cont > 1 else ' = ', end = '')
      f *= cont
      cont -= 1

      print(f'{f}')