#Crie um programa em Python que simule uma calculadora básica, lendo três valores inteiros a, b, e c correspondentes respectivamente a uma operação (a) e dois operandos (b e c).

#Os seguintes padrões de codificação foi adotado para sinalizar a operação desejada:

#Caso a seja 1, deve ser apresentada a soma: b mais c;
#Caso a seja 2, deve ser apresentada a subtração: b menos c;
#Caso a seja 3, deve ser apresentada a multiplicação: b vezes c;
#Caso a seja 4, o valor de c deve ser verificado e se não for zero, apresentada a divizão: b divido por c; Entretanto se c for zero, a mensagem "impossível fazer a divisão" deve ser apresentada.
#Caso a não seja qualquer um dos valores descritos, a mensagem "opção inválida" deverá ser apresentada.
a = int(input())
b = int(input())
c = int(input())
if a == 1:
  print(b+c)
elif a == 2:
  print(b-c)
elif a == 3:
  print(b*c)
elif a == 4:
  if c != 0:
    print(b/c)
  else:
    print('impossível fazer a divisão')
else:
  print('opção inválida')
