#EXERCICIO 9..

#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.




soma_dos_quadrados = []
for i in range(1,11):
    numeros = int(input(f"Digite o {i}º numero inteiro: ")) ** 2
    soma_dos_quadrados.append(numeros)
    listsum = sum(soma_dos_quadrados)
print(f"A soma dos quadrados dos numeros digitados é {listsum}")

