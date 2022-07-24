#EXERCICIO 9...

#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

tamanho_cpf = 14

cpf = input('Por favor insira seu cpf: ')
flag = True

if(len(cpf) != tamanho_cpf):
  flag = False
elif((cpf[3] != '.') or (cpf[7] != '.') or (cpf[-3] != '-')):
  flag = False

for i in range(tamanho_cpf):
  if((i != 3) and (i != 7) and (i != 11)):
    c = cpf[i]
    if (not c.isdigit()):
      flag = False


if(flag):
  print('Formato de CPF valido.')

else:
  print('O CPF informado não tem um formato valido')

  