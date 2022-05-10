'''
Faça um programa em Python que receba e armazene 10 números inteiros em uma lista.

Após a entrada dos 10 números, solicite ao usuário um valor, faça a busca deste número na lista e emita a mensagem NÚMERO EXISTE 
caso o número informado pelo usuário esteja na lista de entrada ou NÚMERO NÃO EXISTE se o número informado não for localizado na lista.
'''
numeros = []
for i in range(10):
    num = int(input())
    numeros.append(num)
comparado = int(input())
if comparado in numeros:
    print('NÚMERO EXISTE')
else:
    print('NÚMERO NÃO EXISTE')
