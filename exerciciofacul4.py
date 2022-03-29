#Implemente um programa em Python que leia as seguinte informações e nesta ordem,

#a distância em quilômetros (km) de um percurso e
#a quantidade de litros de gasolina gasto por um carro para fazer este percurso.
#O programa deve calcular e mostrar o consumo do carro em km/litros e na linha abaixo mostrar uma mensagem de acordo com a tabela:

#TEXTOS DE SAÍDA
#CONSUMO	KM/L	MENSAGEM
#Menor que	8	VENDA O CARRO
#Entre	8 e 12	CARRO ECONÔMICO
#Maior	12	CARRO SUPER ECONÔMICO
d = float(input())
ql = int(input())
consumo = d/ql
print(consumo)
if consumo < 8:
  print('VENDA O CARRO')
elif 7 < consumo < 13:
  print('CARRO ECONÔMICO')
else:
  print('CARRO SUPER ECONÔMICO')
