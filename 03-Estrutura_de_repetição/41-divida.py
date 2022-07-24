#EXERCICIO 41..

#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

#Os juros e a quantidade de parcelas seguem a tabela abaixo:

#      Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#      1                           0
#      3                           10
#      6                           15
#      9                           20
 #     12                          25
#Exemplo de saída do programa:

#    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela

#        R$ 1.000,00     0               1                       R$  1.000,00
#        R$ 1.100,00     100             3                       R$    366,00
#        R$ 1.150,00     150             6                       R$    191,67

V_parcelas = []
listaparcelas = []
V_juros = []
V_dividas = []

divida = float(input('Valor da divida: R$ '))

Q_parcelas = 1
per_juros = 1
V_divida = divida * per_juros
V_juro = V_divida - divida
V_parcela = divida / Q_parcelas

V_dividas.append(V_divida)
V_juros.append(V_juro)
V_parcelas.append(V_parcela)
listaparcelas.append(Q_parcelas)
Q_parcelas += 2

per_juros = 1.1 

for c in range(0,13,3):

    V_divida = divida * per_juros
    V_juro = V_divida - divida
    V_parcela = V_divida / Q_parcelas

    V_dividas.append(V_divida)
    V_juros.append(V_juro)
    V_parcelas.append(V_parcela)
    listaparcelas.append(Q_parcelas)
    per_juros += 0.05
    Q_parcelas += 3




print('\n' * 2) 



print('### Valor da Dívida ### Valor dos Juros ### Quantidade de Parcelas ### Valor da Parcela ###')
print('------------------------------------------------------------------------------------------- \n')
cont = 0
while cont < 5:

    print(f'      R$ {V_dividas[cont]:.2f}               R$ {V_juros[cont]:.2f}             {listaparcelas[cont]}          \
              R$ {V_parcelas[cont]:.2f}' if cont < 1 else f'      R$ {V_dividas[cont]:.2f}               R$ {V_juros[cont]:.2f}    \
                     {listaparcelas[cont]}                    R$ {V_parcelas[cont]:.2f}' )
    cont += 1

