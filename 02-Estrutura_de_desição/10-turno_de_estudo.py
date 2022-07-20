#EXERCICIO 10...

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Olá, informe em qual turno você estuda.\n Digite M para matutino, V para vespertino ou N para noturno. ').upper()

if turno == 'M':
  print('Bom dia!')
elif turno == 'V':  #elif se ussa sempre que quiser adicionar uma condição na condição ja existente. 
  print('Boa tarde!')
elif turno == 'N':
  print('Boa noite!')
else:
  print('Valor invalido!')