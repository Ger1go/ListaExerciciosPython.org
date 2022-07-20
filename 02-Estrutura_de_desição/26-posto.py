# EXERCICIO 26...

#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#-Álcool:

#até 20 litros, desconto de 3% por litro

#acima de 20 litros, desconto de 5% por litro

#-Gasolina:

#até 20 litros, desconto de 4% por litro

#acima de 20 litros, desconto de 6% por litro

#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 2,50 o preço do litro do álcool é 1,90.

preço_a = 1.90
preço_g = 2.50


com = input('Escolha o tipo de combustivel : \n *Digite (A) para álcool (R$ 1.90 x L): \n *Digite (G) para gasolina (R$ 2.50 x L):  ').upper()
litros = int(input('Por favor, digite a quantidade de litros que deseja abastecer: \n'))

if com == 'A'and litros <= 20 :
    print('Você escolheu Álcool, pela quantidade que vai abastecer tem um desconto do 3 %! \n ')
    compra_a = litros * preço_a 
    desc =  (compra_a * 1.03) - compra_a
    total_a = compra_a - desc
    print(f'Valor total a ser pago: R$ {total_a}')
elif com == 'A'and litros > 20 :
    print('Você escolheu Álcool, pela quantidade que vai abastecer tem um desconto do 5 %! \n ')
    compra_a = litros * preço_a 
    desc =  (compra_a * 1.05) - compra_a
    total_a = compra_a - desc
    print(f'Valor total a ser pago: R$ {total_a}')

#------------------------------------------------------

if com == 'G'and litros <= 20 :
    print('Você escolheu Gasolina, pela quantidade que vai abastecer tem um desconto do 4 %! \n ')
    compra_g = litros * preço_g 
    desc =  (compra_g * 1.04) - compra_g
    total_g = compra_g - desc
    print(f'Valor total a ser pago: R$ {total_g}')
elif com == 'G'and litros > 20 :
    print('Você escolheu Gasolina, pela quantidade que vai abastecer tem um desconto do 6 %! \n ')
    compra_g = litros * preço_g 
    desc =  (compra_g * 1.06) - compra_g
    total_g = compra_g - desc
    print(f'Valor total a ser pago: R$ {total_g}')