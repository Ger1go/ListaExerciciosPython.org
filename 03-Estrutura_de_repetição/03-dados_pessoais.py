#EXERCICIO 3 ..

#Faça um programa que leia e valide as seguintes informações:

#Nome: maior que 3 caracteres;

#Idade: entre 0 e 150;

#Salário: maior que zero;

#Sexo: 'f' ou 'm';

#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: \n')
while len(nome) <=3:
    nome = input('Seu nome deve ter mais de 3 carateres. \n Digite seu nome novamente: ')
id = int(input('Digite a sua idade: \n'))
while (id < 0) or ( id > 150):
    id = int(input('Sua idade deve ser entre 0 e 150 anos. \n Digite sua idade novamente: '))
sal = int(input('Digite seu salário: \n'))
while sal <= 0:
    sal = int(input('Seu salario deve ser maior que 0. \n Digite seu salario novamente: '))
sex = input('Digite seu sexo (f ou m ): \n').upper()
while (sex != 'F') and (sex != 'M'):
    sex = input('Dado invalido. \n Digite f ou m para informar seu sexo biologico: ').upper()
est = input('Digite seu estado civil, s, c, v, d : \n')
while (est != 's') and (est != 'c') and (est != 'v') and (est != 'd'):
    est = input("Dado invalido. \n Digite seu estado civil utilizando 's', 'c', 'v' ou 'd': ")