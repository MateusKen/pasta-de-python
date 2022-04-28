"""
Faça um programa em Python com uma função chamada valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.

 A função valorPagamento, que você irá escrever, recebe por parâmetro o valor da prestação e o número de dias em atraso, 
  calcula e retorna o valor a ser pago. O cálculo do valor a ser pago é feito da seguinte forma:

- Para pagamentos sem dias de atraso, cobrar o valor da prestação,

- Quando houver atraso, cobrar 3% de multa e juros de 0,1% por dia de atraso.

O programa possui a função principal (def main()), já escrita na questão, 
que solicita ao usuário o valor da prestação e o número de dias em atraso e mostra o valor retornado pela função que você irá escrever, 
desta forma na caixa Answer coloque apenas a função solicitada.
"""

def valorPagamento (valor, dias):
  if (dias == 0):
    return valor
  elif (dias >0):
    multa = valor*3/100
    juros = valor*dias/1000
    return valor + multa+ juros

def main():
    valor = float(input())
    dias = int(input())
    print(valorPagamento(valor,dias))
main()
