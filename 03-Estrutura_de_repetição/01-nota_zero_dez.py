#EXERCICIO 1 .. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
  try:
    n = int(input(' Digite uma nota entre 0 e 10. '))
  except ValueError:
    print('Deve ser fornecido um valor inteiro')
  else:
    if 0 < n <= 10:
      print (f'O numero fornecido é {n}.')
      break
    else:
      print('O número deve estar entre 0 e 10')
      