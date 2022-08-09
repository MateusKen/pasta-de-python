'''
(1) Imagine que o Python não possui mais o operador de multiplicação (*), por sorte os matemáticos definiram que 
a multiplicação pode ser definida através de somas sucessivas:
a*b = a + a ...+ a ou seja a somado b vezes. 
Para a =4 e b = 5 teremos 4+4+4+4+4, ou seja, 4 somado 5 vezes. 
Escreva a função def mult(a, b): que tem como entrada a e b, 
a função calcula e devolve a multiplicação de a*b utilizando a regra acima.

def mult(a,b):
  total = 0
	for i in range(b):
    total += a
	return a 

a = int(input())
b = int(input())

print(mult(a,b))
'''

'''
(2) Imagine agora que o Python não possui o operador de potência (**), sabemos que a potência 
pode ser definida através de multiplicações sucessivas:xy = x * x ...* x ou seja x multiplicado y vezes. 
Para x =4 e y = 5 teremos 4*4*4*4*4, ou seja, 4 multiplicado 5 vezes. 

Escreva a função  def potencia(x,y): que tem como entrada x e y e calcule a potência de xy.


def potencia(x,y):
	total = 0
	for i in range(y):
		total = x*x
	return x

x = int(input())
y = int(input())

print(potencia(x,y))
'''

'''
(3) Considere o problema de encontrar todos números primos existentes entre N1 e N2 (inclusive), 
em que N1 e N2 são números naturais lidos. Para resolver o problema escreva a função def ehPrimo(n), 
que verifica se um número é primo, com a função pronta escreva um programa que utiliza a função ehPrimo() 
para resolver o problema descrito acima. 

def ehPrimo(n):
	cont = 0
	for i in range(1, n + 1):
    	if n % i == 0:
      		cont += 1
  	if cont == 2:
    	return True  
  	else:
    	return False

def main(a,b):
	for i in range(a,b):
		print(ehPrimo(i))

a = int(input())
b = int(input())

print(main(a,b))
'''
