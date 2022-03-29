#Escreva um programa em Python que leia um número inteiro de 3 dígitos. Em seguida analise-o para identificar se o algarismo da centena é par ou ímpar, imprimindo na tela a mensagem correspondente segundo a tabela a seguir.

#TEXTOS DA MENSAGEM DE SAÍDA
#Situação	Texto Esperado
#1. Se o número não tiver 3 dígitos	VALOR FORA DO INTERVALO
#2. Se o número da centena é par	CENTENA PAR
#3. Se o número da centena é impar	CENTENA IMPAR
 
numero = int(input())
if 99<numero<1000:
  if 999>=numero>=900:
    print('CENTENA IMPAR')
  elif 899>= numero>=800:
    print('CENTENA PAR')
  elif 799>=numero>=700:
    print('CENTENA IMPAR')
  elif 699>= numero>=600:
    print('CENTENA PAR')
  elif 599>=numero>=500:
    print('CENTENA IMPAR')
  elif 499>= numero>=400:
    print('CENTENA PAR')
  elif 399>=numero>=300:
    print('CENTENA IMPAR')
  elif 299>= numero>=200:
    print('CENTENA PAR')
  elif 199>=numero>=100:
    print('CENTENA IMPAR')
else:
  print('VALOR FORA DO INTERVALO')
