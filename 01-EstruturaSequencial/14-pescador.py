#EXERCICIO 14.. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas

peso_dos_peixes = float(input('Digite o peso do peixes: '))

if peso_dos_peixes > 50:
    execesso = peso_dos_peixes -50
    print(f'Peso excedente: {execesso:.2f}KG')
    if execesso > 1:
        multa = execesso * 4
    print(f'A multa a ser paga é: R${multa}')
elif peso_dos_peixes < 50:
    print(f'Peso do peixe: {peso_dos_peixes:.2f}KG \nNão será necessário pagar multa') 