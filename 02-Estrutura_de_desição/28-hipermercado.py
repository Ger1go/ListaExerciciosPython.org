#EXERCICIO 28..

#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                    Até 5 Kg             Acima de 5 Kg
# File Duplo      R$ 5,90 por Kg          R$ 4,80 por Kg
# Alcatra         R$ 6,90 por Kg          R$ 5,80 por Kg
# Picanha         R$ 7,90 por Kg          R$ 6,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.



print()
print('>>>>>>>>>>>>>>>>>>>>CARNES EM PROMOÇÃO PARA COMPRAS POR KILO !!!<<<<<<<<<<<<<<<<<<<<')
print()

print('                     Até 5 Kg             Acima de 5 Kg \n \
 File Duplo      R$ 5,90 por Kg          R$ 4,80 por Kg \n \
 Alcatra         R$ 6,90 por Kg          R$ 5,80 por Kg \n \
 Picanha         R$ 7,90 por Kg          R$ 6,80 por Kg')
print()

t_carne = int(input('Escolha a carne da sua preferencia! Digite o número correspondente ao tipo de carne: \n 1) File Duplo \n 2) Alcatra \n 3) Picanha.\n '))

if t_carne > 3:
    print('OPÇÃO INVALIDA!')
  
else:
  kg = int(input('Digite quantos kg de carne vai comprar?: '))

  Fpagamento = input('Pagamento com cartão de credito ? (Tem desconto 5%): (S/N) \n').upper()




  if t_carne == 1 and kg <= 5:
    t_carne = 'File Duplo'
    preço = float(5.90 * kg)

  elif t_carne == 1 and kg > 5:
    t_carne = 'File Duplo'
    preço =float(4.80 * kg)

  elif t_carne == 2 and kg <= 5:
    t_carne = "Alcatra"
    preço = float(6.90 * kg)
  elif t_carne == 2 and kg > 5:
    t_carne = "Alcatra"
    preço = float(5.80 * kg)

  elif t_carne == 3 and kg <= 5:
    t_carne = "Picanha"
    preço = float(7.90 * kg)
  elif t_carne == 3 and kg > 5:
    t_carne = "Picanha"
    preço = float(6.80 * kg)

  print()
  print('>>>>>>>>>>>>>>>>>>>>NOTA FISCAL<<<<<<<<<<<<<<<<<<<<')
  print()

  print(f'TIPO DE CARNE:----------{t_carne}')
  print(f'QUANTIDADE:-------------{kg} kg')
  print(f'PREÇO TOTAL:------------R$ {preço}')

  if Fpagamento == 'S':
    Fpagamento = 'Cartão de Credito'
    desc = ((preço * 1.05) - preço)
    print(f'FORMA DE PAGAMENTO:-----{Fpagamento}')
    print(f'VALOR DE DESCONTO :-----R$ {desc:.2f}')
    print(f'VALOR A PAGAR:----------R$ {(preço - desc):.2f}')
  else:
    Fpagamento = 'Dinheiro'
    print(f'FORMA DE PAGAMENTO:-----{Fpagamento}')
    print(f'VALOR DE DESCONTO :-----R$ 0 ')
    print(f'VALOR A PAGAR:----------R$ {(preço)}')
