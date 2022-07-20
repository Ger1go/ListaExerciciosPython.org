#EXERCICIO 11.. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

#a- O produto do dobro do primeiro com metade do segundo .
#b- A soma do triplo do primeiro com o terceiro.
#c- O terceiro elevado ao cubo.

print("Vamos fazer um Programa que peça 2 números inteiros e um número real, para que logo calcule e mostre: \n a- O produto do dobro do primeiro com metade do segundo .\n b- A soma do triplo do primeiro com o terceiro. \n c- O terceiro elevado ao cubo.")
print("\n \n")
int1 = int(input("Digite o primeiro numero inteiro: "))
int2 = int(input("Digite o segundo numero inteiro: "))
real = float(input("Digite um numero real: "))

a = float(int1*2 + (int2/2))
print(f"\n O produto do dobro do primeiro com metade do segundo é: {a}")
b = float(int1*3 + real)
print(f"\n A soma do triplo do primeiro com o terceiro é: {b} ")
c = float(real**3)
print(f"\n O terceiro elevado ao cubo é: {c} ")