#EXERCICIO 2 .. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
  loguin = input('Digite seu loguin: ')
  senha = input('Digite a sua senha:')
  
  if senha == loguin:
    print('Senha e loguin não podem ser iguais. ')
  else:
    print('OK')
    break
    