#EXERCICIO 31..

#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

#    Lojas Tabajara 
#    Produto 1: R$ 2.20
#    Produto 2: R$ 5.80
#    Produto 3: R$ 0
#    Total: R$ 9.00
#    Dinheiro: R$ 20.00
#    Troco: R$ 11.00
#    ...

while True:
    print( "Bem vindo a Lojas Tabajara \n")
    venda = []
    P = 1
    cont = 1
    while (P != 0):
      P = float(input(f"Produto {cont} R$:" ))
      venda.append(P)
      cont += 1

    else:
      total = sum(venda)
      print(f'Total: R${total} ')
      din = float(input("Dinheiro: R$ "))
      troco = din - total
      print(f'Troco R$ {troco}')

    reset = input("pressione 0 para reset, 1 para encerrar: ")

    if reset == "0":
      print("\n"*2, "Obrigado pela sua compra. \n" )
      print('------------------------------------------------')
      print(' PROXIMO CLIENTE: \n')
      continue

    else:
      print("\n \n Obrigado pela sua compra. Caixa encerrado.")

      break