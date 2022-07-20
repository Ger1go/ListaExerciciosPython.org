#EXERCICIO 19... Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades

#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


num = int(input('informe um numero inteiro: '))

centenas = int(num / 100)
dezenas = int((num - (centenas * 100)) / 10)
unidades = int(num - (centenas * 100) - (dezenas * 10))

extenso = ''

if centenas > 0:
  extenso = extenso + str(centenas)
  if centenas > 1 :
    extenso = extenso + ' centenas '
  else:
    extenso = extenso + ' centena '

if dezenas > 0:
  if unidades == 0 and centenas != 0: 
    extenso = extenso + 'e '
  extenso = extenso + str(dezenas)
  if dezenas > 1 :
    extenso = extenso + ' dezenas '
  else:
    extenso = extenso + ' dezena '
    
if unidades > 0:
  if centenas != 0 or dezenas != 0:
    extenso = extenso + 'e '
  extenso = extenso + str(unidades)
  if unidades > 1:
    extenso = extenso + ' unidades'
  else:
    extenso = extenso + ' unidade'


if extenso == 0: 
  print( '0 não tem centenas, nem dezenas, nem unidades. FIM DO PROGRAMA')


print(extenso)



