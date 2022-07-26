#EXERCICIO 11..

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

#salários até 280,00 reais (incluindo) : aumento de 20%

#salários entre 280,00 reais e 700,00 reais : aumento de 15%

#salários entre 700,00 reais e 1500,00 reais : aumento de 10%

#salários de 1500,00 reais em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

#o salário antes do reajuste;

#o percentual de aumento aplicado;

#o valor do aumento;

#o novo salário, após o aumento.

print('>>>>>>>>>>>>>>>PARABENS VOCÊ RECEBEU UM AUMENTO! <<<<<<<<<<<<<< \n')

salario = float(input('Digite o seu salário atual para calcular o seu aumento: '))


if salario <= 280.00:
  print(f"Seu salário antes do aumento era de R${salario:.2f}")
  print("Reajustado em 20% é:R$ {:.2f}".format(salario*1.2))
  print('O seu aumento foi de: R$ {:.2f}'.format((salario*1.2)-(salario)))
  
elif salario > 280.00 and salario <= 700.00:
  print(f"Seu salário antes do aumento era de R${salario:.2f}")
  print("Reajustado em 15% é:R$ {:.2f}".format(salario*1.15))
  print('O seu aumento foi de: R$ {:.2f}'.format((salario*1.15)-(salario)))
 
elif salario > 700.00 and salario <= 1500.00:
  print(f"Seu salário antes do aumento era de R${salario:.2f}")
  print("Reajustado em 10% é:R$ {:.2f}".format(salario*1.1))
  print('O seu aumento foi de: R$ {:.2f}'.format((salario*1.1)-(salario)))
  
elif salario > 1500.00:
  print(f"Seu salário antes do aumento era de R${salario:.2f}")
  print("Reajustado em 5% é:R$ {:.2f}".format(salario*1.05))
  print('O seu aumento foi de: R$ {:.2f}'.format((salario*1.05)-(salario)))