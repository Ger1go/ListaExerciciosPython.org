#EXERCICIO 16..

#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe 200 por semana mais 9 por cento de suas vendas brutas daquela semana.

#Por exemplo, um vendedor que teve vendas brutas de 3000 em uma semana recebe 200 mais 9 por cento de 3000, ou seja, um total de 470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

#200 - 299

#300 - 399

#400 - 499

#500 - 599

#600 - 699

#700 - 799

#800 - 899

#900 - 999

#1000 em diante

#Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

salario_da_semana = 200
vendedores = [0]*9

for i in range(0, 12):
    valor_venda_bruta = float(input(f'Informe o valor das vendas brutas do {i+1}° vendedor: '))
    salario = valor_venda_bruta * 0.09 + salario_da_semana
    indice = int(salario / 100) - 1
    if (indice > 9):
        indice = 9
    elif (indice < 1):
        indice = 1
    print(f'O salario do {i+1}° vendedor é de R$ {salario}, correspondente á  {indice}a faixa salarial.\n' )
    vendedores[indice-1] += 1

for i in range(0, 9):
    print(i * 100 + 200,' ---> ', (i + 1) * 100 + 199, ':', vendedores[i]) 

    