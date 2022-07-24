#EXERCICIO 37..

#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

cod_clientes = [] 
altura_clientes = []
peso_clientes = []

cli = 1
codigo = 1

while codigo != 0:
 print(f'Cliente n°{cli}')
 codigo = int(input('Digite o código: '))
 if codigo == 0:
   continue
 altura = int(input('Digite a altura: '))
 peso = int(input('Digite o peso: '))
 print('-------')
 cod_clientes.append(codigo)
 altura_clientes.append(altura)
 peso_clientes.append(peso)
 cli += 1

else:
  alto = altura_clientes.index(max(altura_clientes)) 
  baixo = altura_clientes.index(min(altura_clientes))
  gordo = peso_clientes.index(max(peso_clientes))
  magro = peso_clientes.index(min(peso_clientes))
  print('---------------------------------------------','\n'*2)
  print(f'O cliente mais alto é o do codigo {cod_clientes[alto]}. \n Com uma altura de {altura_clientes[alto]}cm e um peso de {peso_clientes[alto]}Kg.\n')
  print(f'O cliente mais baixo é o do codigo {cod_clientes[baixo]}. \n Com uma altura de {altura_clientes[baixo]}cm e um peso de {peso_clientes[baixo]}Kg.\n')
  print(f'O cliente mais gordo é o do codigo {cod_clientes[gordo]}. \n Com uma altura de {altura_clientes[gordo]}cm e um peso de {peso_clientes[gordo]}Kg.\n')
  print(f'O cliente mais magro é o do codigo {cod_clientes[magro]}. \n Com uma altura de {altura_clientes[magro]}cm e um peso de {peso_clientes[magro]}Kg.\n')
  print('---------------------------------------------','\n'*2)

  media_altura = sum(altura_clientes) / len(altura_clientes)
  media_peso = sum(peso_clientes) / len(peso_clientes)
  print(f'A média das alturas dos clientes é de {media_altura}cm.')
  print(f'A média do peso dos clientes é de {media_peso}kg.')

  
