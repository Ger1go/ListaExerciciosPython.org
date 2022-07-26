#EXERCICIO 7...

#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

relatorio_do_dia = []
def valorPagamento(V_prestacao, D_atraso):
    return (V_prestacao + (V_prestacao * 0.03)) + ( D_atraso + (D_atraso * 0.001))

while True:
  V_prestacao = int(input('Informe o valor da prestação, ou digite "0" para finalizar: R$'))
  if V_prestacao == 0:
    break
  D_atraso = int(input('Informe os dias de atráso: '))
  total = valorPagamento(V_prestacao, D_atraso)
  print(f'O valor a ser pago é : R${total:.2f}\n')
  relatorio_do_dia.append(total)

print('')
print(('>')*12,'RELATORIO DO DIA',('<')*12)
Q_prestacoes = len(relatorio_do_dia)
V_prestacoes = sum(relatorio_do_dia)
print(f'\nQUANTIDADE DE PRESTAÇÕES PAGAS NO DIA: {Q_prestacoes}\nVALOR TOTAL DE PRESTAÇÕES PAGA NO DIA: R${V_prestacoes:.2f}')

