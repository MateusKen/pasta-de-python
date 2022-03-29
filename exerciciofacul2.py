#Desenvolva um programa em Python que leia um número inteiro e maior que zero a partir do teclado e apresente:

#1. a raiz quadrada deste número, caso ele seja par; e
#2. o quadrado do número, caso ele seja ímpar.
#Importante:

#nesta questão faça uso da função matemática para ambos os casos (raiz quadrada e quadrado).
#considere que o usuário informará um número positivo e diferente de zero, portanto não é necessário validar a entrada dos dados.
numero = float(input())
if numero%2 == 0:
  print(numero**(1/2))
else:
  print(numero**2)
