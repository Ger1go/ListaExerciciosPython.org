#EXERCICIO 15..

#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

nesimo = int(input('Digite o número referente ao termo que deseja conhecer da sequancia de fibonacci: '))


t1 = 0
t2 = 1

print(f'{t1}, {t2}', end ='')

cont = 3
while cont <= nesimo:
    t3 = t1 + t2
    print(f', {t3}', end = '')
    t1 = t2
    t2 = t3
    cont +=1
