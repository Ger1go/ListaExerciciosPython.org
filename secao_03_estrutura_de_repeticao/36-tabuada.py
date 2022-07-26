#EXERCICIO 36..

#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:}

#          Montar a tabuada de: 5
#          Começar por: 4
#          Terminar em: 7

#          Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#            5 X 4 = 20
#            5 X 5 = 25
#            5 X 6 = 30
#            5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

num = int(input('Montar a tabuada de: '))
com = int(input('Começar por: '))
ter = int(input('Terminar em: '))

if com < ter:

    print('\n')
    print(f'Vou montar a tabuada de {num}, começando em {com} e terminando em {ter}:')

    cont = 0
    tab = com


    while tab <= ter:
      res = int(num * tab)
      print(f'{num} X {tab} = {res}')
      cont = cont +1
      tab = tab +1
          
else:
  print('O começo deve ser menor que o termino! \n')
  