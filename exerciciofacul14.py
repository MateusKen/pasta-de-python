'''
3) Escreva uma função que recebe dois vetores inteiros A[] e B[], em seguida, a sua função efetua a INTERSECÇÃO entre os vetores, ou seja, os elementos em comum entre os dois vetores, ao final sua função retorna uma String com a resposta. Os vetores dados não possuem valores duplicados e não estão ordenados.
Exemplo:
A[] = { 7, 2, 5, 8, 4} e B[]= {4, 2, 9, 5} então 
A  B = {2, 5, 4}

	A[] = { 3, 9, 11} e B[]= {2, 6, 1} então 
A  B= {}
'''

'''
import random

def geraLista(lista):
    for i in range(0,10):
        lista.append(random.randint(0,9))
    return lista

def interseccao(lista1, lista2):
    resposta = ''
    for i in lista1:
        for j in lista2:
            if i == j:
                resposta += str(i)
                break
    return resposta
def main():
    lista1 = []
    lista2 = []
    geraLista(lista1)
    geraLista(lista2)
    print(lista1)
    print(lista2)
    print(interseccao(lista1, lista2))
    


main()
'''

'''
4) Repita o exercício anterior, agora deve ser retornado em uma String os elementos que estão em A[] mas não estão em B[], ou seja, a diferença de A – B, por exemplo:
A[] = { 7, 2, 5, 8, 4} e B[]= {4, 2, 9, 5} então 
A – B = {7, 8 }

A[] = { 3, 9, 11} e B[]= {2, 6, 1} então 
A –  B= {3, 9, 11}
'''

'''
import random

def geraLista(lista):
    for i in range(0,10):
        lista.append(random.randint(0,9))
    return lista

def diferenca(A,B):
    resposta = ''
    achou = False
    for i in A:
        achou = False
        for j in B:
            if i == j:
                achou = True
        if achou == False:
            resposta += str(i)
    return resposta

def main():
    lista1 = []
    lista2 = []
    geraLista(lista1)
    geraLista(lista2)
    print(lista1)
    print(lista2)
    print(diferenca(lista1,lista2))

main()
'''


   
