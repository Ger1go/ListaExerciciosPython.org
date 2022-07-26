#EXERCICIO 12..

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:

#Salário Bruto até 900 (inclusive) - isento

#Salário Bruto até 1500 (inclusive) - desconto de 5%

#Salário Bruto até 2500 (inclusive) - desconto de 10%

#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#    Salário Bruto: (5 * 220)        : R$ 1100,00
#    (-) IR (5%)                     : R$   55,00  
#    (-) INSS ( 10%)                 : R$  110,00
#    FGTS (11%)                      : R$  121,00
#    Total de descontos              : R$  165,00
#    Salário Liquido                 : R$  935,00


print('<<<<<<<<<<<<<<<<<<<<FOLHA DE PAGAMENTO>>>>>>>>>>>>>>>>>>>')

print('Por favor, informe o valor da sua hora e a quantidade de horas trabalhadas no mês.')
v_h= float(input('Valor hora: \n'))
h_t= float(input('Quantidade de horas trabalhadas: \n'))
salario_bruto = v_h * h_t
print(f'Salario bruto :        {salario_bruto}')
print()


INSS = (salario_bruto*1.1) - salario_bruto

if salario_bruto <= 900.00:
  print('(-) IR (0%) :         R$ {:.2f}'.format(0))
  print('(-) INSS (10%):       R$ {:.2f}'.format(INSS))
  print('FGTS (11%):           R$ {:.2f}'.format((salario_bruto*1.11)-salario_bruto))
  print('Total de descontos:   R$ {:.2f}'.format(INSS + 0))
  print('Salario líquido:      R$ {:.2f}'.format((salario_bruto)- (INSS + 0)))

elif salario_bruto <= 1500.00:
  print('(-) IR (5%) :         R$ {:.2f}'.format((salario_bruto*1.05)- salario_bruto))
  print('(-) INSS (10%):       R$ {:.2f}'.format(INSS))
  print('FGTS (11%):           R$ {:.2f}'.format((salario_bruto*1.11)-salario_bruto))
  print('Total de descontos:   R$ {:.2f}'.format(INSS+((salario_bruto*1.05)-salario_bruto)))
  print('Salario líquido:      R$ {:.2f}'.format((salario_bruto)-(INSS+((salario_bruto*1.05)-salario_bruto))))

elif salario_bruto <= 2500.00:
  print('(-) IR (10%) :        R$ {:.2f}'.format((salario_bruto*1.1)- salario_bruto))
  print('(-) INSS (10%):       R$ {:.2f}'.format(INSS))
  print('FGTS (11%):           R$ {:.2f}'.format((salario_bruto*1.11)-salario_bruto))
  print('Total de descontos:   R$ {:.2f}'.format(INSS+((salario_bruto*1.1)-salario_bruto)))
  print('Salario líquido:      R$ {:.2f}'.format((salario_bruto)-(INSS+((salario_bruto*1.1)-salario_bruto))))

elif salario_bruto > 2500.00:
  print('(-) IR (20%) :        R$ {:.2f}'.format((salario_bruto*1.2)- salario_bruto))
  print('(-) INSS (10%):       R$ {:.2f}'.format(INSS))
  print('FGTS (11%):           R$ {:.2f}'.format((salario_bruto*1.11)-salario_bruto))
  print('Total de descontos:   R$ {:.2f}'.format(INSS+((salario_bruto*1.2)-salario_bruto)))
  print('Salario líquido:      R$ {:.2f}'.format((salario_bruto)-(INSS+((salario_bruto*1.2)-salario_bruto))))

