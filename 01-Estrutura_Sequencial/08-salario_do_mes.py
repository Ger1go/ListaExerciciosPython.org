#EXERCICIO 8.. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Vamos calcular seu salario")
valor_hora = int(input("Informe o seu valor hora:"))
quant_horas = int(input("Informe quantas horas você trabalha no mês: "))
resposta = valor_hora * quant_horas
print(f"seu salario é de : R${resposta} por mes ")

