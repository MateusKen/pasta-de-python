''
1) função que cria uma lista com 50 valores
2) função que soma todos os valores de uma lista
3) função que recebe um número e diz se ele está na lista, e quantas vezes ele se repete
''
import random

def geraLista(lista):
  for x in range(50):
    lista.append(random.randint(1,10))
  return lista

def somaLista(lista):
  soma = 0
  for x in range(len(lista)):
    soma += lista[x]
  return soma
  
def repetidosLista(lista):
  vezes = 0
  for x in range(len(lista)):
    if lista[x] == desejado:
       vezes += 1
  return vezes
  
def main():
  lista = []
  lista = geraLista(lista)
  print(somaLista(lista))
  print(lista)
  desejado = int(input('Qual número você deseja saber se repete?   '))
  if desejado in lista:
    repetidosLista(lista,desejado)
  else:
    print('O número desejado não está na lista')
  
main()
