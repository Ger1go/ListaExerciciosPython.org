#EXERCICIO 4...

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

população_a = 80_000
população_b = 200_000
taxa_de_crescimento_de_a = 1.03
taxa_de_crescimento_de_b = 1.015
anos = 0 

while população_a < população_b:
    print(f'#################### POPULAÇÃO NO ANO {anos} #################### \n ')
    print(f'População de A: {população_a}')
    print(f'População de B: {população_b}')
    print()
    anos += 1
    população_a *= taxa_de_crescimento_de_a
    população_b *= taxa_de_crescimento_de_b

    