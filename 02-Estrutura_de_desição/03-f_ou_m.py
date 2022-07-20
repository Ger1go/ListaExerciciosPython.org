#EXERCICIO 3.. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo = input('Digite seu sexo."M" PARA MASCULINO, "F" PARA FEMENINO, "I" PARA INDEFINIDO:  ').upper()
if sexo == 'F':
  print('FEMENINO')
elif sexo == 'M':
  print('MASCULINO')
elif sexo == 'I':
  print('INDEFINIDO')
else:
  print('SEXO INVALIDO')