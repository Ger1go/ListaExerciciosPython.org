#EXERCICIO 21.. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

num = int(input('Digite o valor do saque que deseja realizar, lembrando que o mínimo permitido é de R$10 e o máximo é de R$600: '))
if num > 600:
  print('Não é permitido o saque de mais de R$ 600, digite outro valor.')
elif num < 10:
  print('Não é permitido o saque de menos de R$ 10, digite outro valor.')
else:


  centenas_str = dezenas_str = unidades_str = ''

  partes_numericas = 0 



#centenas

  centenas_int, num = divmod(num, 100)


  if centenas_int == 1:
   centenas_str = 'uma nota de 100'
   partes_numericas +=1
  elif centenas_int > 1 and centenas_int <= 6:
    centenas_str = f'{centenas_int} notas de 100'
    partes_numericas +=1



#dezenas


  dezenas_int, num = divmod(num, 10)



  if dezenas_int == 1:
   dezenas_str = 'uma nota de 10'
   partes_numericas +=1
  elif dezenas_int > 1 and dezenas_int < 5:
    dezenas_str = f'{dezenas_int} notas de 10'
    partes_numericas +=1
  elif dezenas_int == 5:
    dezenas_str = 'uma nota de 50,'
    partes_numericas +=1
  elif dezenas_int >= 5:
    dezenas_int = (dezenas_int - 5)
    dezenas_str = f'uma nota de 50, {dezenas_int} de 10 '
    partes_numericas +=1

 

#unidades    

  unidades_int = num //1


  if unidades_int == 1:
   unidades_str = 'uma nota de 1. '
   partes_numericas +=1
  elif unidades_int > 1 and unidades_int < 5:
    unidades_str = f'{unidades_int} notas de 1.'
    partes_numericas +=1
  elif unidades_int == 5:
    unidades_str = 'uma nota de 5.'
    partes_numericas +=1
  elif unidades_int >= 5:
    unidades_int = (unidades_int - 5)
    unidades_str = f' uma nota de 5 e {unidades_int} de 1. '


#partes

  if centenas_int < 6 and partes_numericas == 0: 
   print('Numero 0, no possui centenas, dezenas ou unidades.')
  elif partes_numericas == 1: 
   print(centenas_str + dezenas_str + unidades_str)
  elif partes_numericas == 3:
   print(f'{centenas_str}, {dezenas_str} e {unidades_str}')
  elif partes_numericas == 2:
    if centenas_str != '':
     segunda_parte = dezenas_str + unidades_str
     print(f'{centenas_str}, {segunda_parte}')
    else:
     print(f'{dezenas_str} e {unidades_str}') 