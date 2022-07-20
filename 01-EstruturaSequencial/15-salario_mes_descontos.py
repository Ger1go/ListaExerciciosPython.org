#EXERCICIO 15..Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

#Salário Bruto : R$

#IR (11%) : R$

#INSS (8%) : R$

#Sindicato ( 5%) : R$

#= Salário Liquido : R$

#Obs.: Salário Bruto - Descontos = Salário Líquido.


print('Olá trabalhador! Vamos calcular a sua folha de pagamento com salario bruto, liquido e todos os seus descontos.')
sal_hora = float(input('Informe por favor qual é o seu valor hora: '))
quant_horas = float(input('Informa também a quantidade de horas trabalhadas por mês: '))
salario_bruto = sal_hora * quant_horas

IR = float(salario_bruto * 11 / 100)
INSS = salario_bruto * 8 / 100
SINDICATO = salario_bruto * 5 / 100
sal_liq = salario_bruto - IR - INSS - SINDICATO
print('\n \n \n ')

print('>>>>>>>>>>>>>>>>>>>>FOLHA DE PAGAMENTO<<<<<<<<<<<<<<<<<<<< \n \n \n')

print(f' * Salario bruto = R$ {salario_bruto:.2f} \n')
print(f' * IR = R$ {IR:.2f} \n')
print(f' * INSS = R$ {INSS:.2f}\n')
print(f' * SINDICATO = R$ {SINDICATO:.2f}\n')
print(f' * Total de descontos = R$ {IR + INSS + SINDICATO} \n ')
print(f' * Salario liquido = R$ {sal_liq:.2f}  \n')

