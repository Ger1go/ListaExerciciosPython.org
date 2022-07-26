#EXERCICIO 33..

#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

print('DEPARTAMENTO ESTADUAL DE METEOROLOGIA \n')

temp = []
quant = int(input('Quantas temperaturas deseja registrar?:  \n'))

for c in range(quant):
  graus = int(input('Por favor insira a temperatura a ser registrada: '))
  print('°C')
  temp.append(graus)

media = float(sum(temp) / len(temp))
maior = max(temp)
menor = min(temp)
print(f'A maior temperatura registrada foi: {maior}°C . ')
print(f'A menor temperatura registrada foi: {menor}°C . ')
print(f'A temperatura média foi de: {media} °C')
