#EXERCICIO 11..

#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

ELEMENTOS = 10
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
for i in range(ELEMENTOS):
    vetor1.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 1: "))
    )
for i in range(ELEMENTOS):
    vetor2.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 2: "))
    )
for i in range(ELEMENTOS):
    vetor3.append(
        int(input(f"Entre com o {i+1}º número inteiro para o vetor 3: "))
    )


for i in range(ELEMENTOS):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print("O vetor com os elementos intercalados dos vetores 1 e 2 é: ")
for i in range(30):
    print(vetor4[i], end=" ")
    